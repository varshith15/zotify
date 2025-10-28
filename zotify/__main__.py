#! /usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path

from zotify.app import App
from zotify.config import CONFIG_PATHS, CONFIG_VALUES
from zotify.utils import OptionalOrFalse

VERSION = "0.9.7"


def main():
    parser = ArgumentParser(
        prog="zotify",
        description="A fast and customizable music and podcast downloader",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Print version and exit",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Display full tracebacks",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=CONFIG_PATHS["conf"],
        help="Specify the config.json location",
    )
    parser.add_argument(
        "-l",
        "--library",
        type=Path,
        help="Specify a path to the root of a music/playlist/podcast library",
    )
    parser.add_argument(
        "-o", "--output", type=str, help="Specify the output file structure/format"
    )
    parser.add_argument(
        "-c",
        "--category",
        type=str,
        choices=["album", "artist", "playlist", "track", "show", "episode"],
        default=["album", "artist", "playlist", "track", "show", "episode"],
        nargs="+",
        help="Searches for only this type",
    )
    parser.add_argument("--username", type=str, default="", help="Account username")
    parser.add_argument("--token", type=str, default="", help="Account token")
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="Download tracks in reverse order (newest first)",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "urls",
        type=str,
        default="",
        nargs="*",
        help="Downloads the track, album, playlist, podcast, episode or artist from a URL or URI. Accepts multiple options.",
    )
    group.add_argument(
        "-d",
        "--download",
        type=str,
        help="Downloads tracks, playlists and albums from the URLs written in the file passed.",
    )
    group.add_argument(
        "-f",
        "--followed",
        action="store_true",
        help="Download all songs from your followed artists.",
    )
    group.add_argument(
        "-lt",
        "--liked-tracks",
        action="store_true",
        help="Download all of your liked songs.",
    )
    group.add_argument(
        "-le",
        "--liked-episodes",
        action="store_true",
        help="Download all of your liked episodes.",
    )
    group.add_argument(
        "-p",
        "--playlist",
        action="store_true",
        help="Download a saved playlists from your account.",
    )
    group.add_argument(
        "-s",
        "--search",
        type=str,
        nargs="+",
        help="Search for a specific track, album, playlist, artist or podcast",
    )

    for k, v in CONFIG_VALUES.items():
        if v["type"] == bool:
            parser.add_argument(
                *v["args"],
                action=OptionalOrFalse,
                default=v["default"],
                help=v["help"],
            )
        else:
            try:
                parser.add_argument(
                    *v["args"],
                    type=v["type"],
                    choices=v["choices"],
                    default=None,
                    help=v["help"],
                )
            except KeyError:
                parser.add_argument(
                    *v["args"],
                    type=v["type"],
                    default=None,
                    help=v["help"],
                )

    parser.set_defaults(func=App)
    args = parser.parse_args()
    if args.version:
        print(VERSION)
    elif args.debug:
        args.func(args)
    else:
        try:
            args.func(args)
        except Exception:
            from traceback import format_exc

            print(format_exc().splitlines()[-1])
            exit(1)
        except KeyboardInterrupt:
            exit(130)


if __name__ == "__main__":
    main()
