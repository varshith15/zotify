![Logo banner](./assets/banner.png)

# Zotify

A customizable music and podcast downloader. \
Formerly ZSp‌otify.

Available on [zotify.xyz](https://zotify.xyz/zotify/zotify) and [GitHub](https://github.com/zotify-dev/zotify). \
Built on [Librespot](https://github.com/kokarare1212/librespot-python).

## Features

- Save tracks at up to 320kbps<sup>**1**</sup>
- Save to most popular audio formats (including **WAV** for DJs!)
- Built in search
- Bulk downloads
- Downloads synced lyrics<sup>**2**</sup>
- Embedded metadata
- Downloads all audio, metadata and lyrics directly, no substituting from other services
- **🚀 NEW: Batch metadata fetching** - Dramatically faster playlist processing
- **🚀 NEW: Smart duplicate detection** - Automatically skips duplicate tracks in playlists
- **🚀 NEW: Intelligent file checking** - Checks for existing files before requesting audio keys (reduces rate limiting)
- **🚀 NEW: Reverse download order** - Download newest tracks first with `--reverse` flag
- **🚀 NEW: Fixed WAV format support** - Proper PCM encoding for lossless audio
- **🚀 NEW: Improved Premium detection** - Works correctly with Spotify Family Plan accounts

**1**: Non-premium accounts are limited to 160kbps \
**2**: Requires premium

## Installation

Requires Python 3.11 or greater. \
Optionally requires FFmpeg to save tracks as anything other than Ogg Vorbis.

Enter the following command in terminal to install Zotify. \
`python -m pip install https://get.zotify.xyz`

## General Usage

### Simplest usage

Downloads specified items. Accepts any combination of track, album, playlist, episode or artists, URLs or URIs. \
`zotify <items to download>`

### Basic options

```
    -p,  --playlist         Download selection of user's saved playlists
    -lt, --liked-tracks     Download user's liked tracks
    -le, --liked-episodes   Download user's liked episodes
    -f,  --followed         Download selection of users followed artists
    -s,  --search <search>  Searches for items to download
         --reverse          Download tracks in reverse order (newest first)
```

### Usage Examples

```bash
# Download a playlist with WAV format for DJ use
zotify https://open.spotify.com/playlist/... --audio-format wav --download-quality very_high

# Download newest tracks first (useful for frequently updated playlists)
zotify https://open.spotify.com/playlist/... --reverse

# Download with all optimizations (automatic duplicate detection and smart skipping)
zotify https://open.spotify.com/playlist/... --audio-format wav --print-skips
```

<details><summary>All configuration options</summary>

| Config key              | Command line argument     | Description                                         | Default                                                    |
| ----------------------- | ------------------------- | --------------------------------------------------- | ---------------------------------------------------------- |
| path_credentials        | --path-credentials        | Path to credentials file                            |                                                            |
| path_archive            | --path-archive            | Path to track archive file                          |                                                            |
| music_library           | --music-library           | Path to root of music library                       |                                                            |
| podcast_library         | --podcast-library         | Path to root of podcast library                     |                                                            |
| mixed_playlist_library  | --mixed-playlist-library  | Path to root of mixed content playlist library      |                                                            |
| output_album            | --output-album            | File layout for saved albums                        | {album_artist}/{album}/{track_number}. {artists} - {title} |
| output_playlist_track   | --output-playlist-track   | File layout for tracks in a playlist                | {playlist}/{playlist_number}. {artists} - {title}          |
| output_playlist_episode | --output-playlist-episode | File layout for episodes in a playlist              | {playlist}/{playlist_number}. {episode_number} - {title}   |
| output_podcast          | --output-podcast          | File layout for saved podcasts                      | {podcast}/{episode_number} - {title}                       |
| download_quality        | --download-quality        | Audio download quality (auto for highest available) |                                                            |
| audio_format            | --audio-format            | Audio format of final track output                  |                                                            |
| transcode_bitrate       | --transcode-bitrate       | Transcoding bitrate (-1 to use download rate)       |                                                            |
| ffmpeg_path             | --ffmpeg-path             | Path to ffmpeg binary                               |                                                            |
| ffmpeg_args             | --ffmpeg-args             | Additional ffmpeg arguments when transcoding        |                                                            |
| save_credentials        | --save-credentials        | Save login credentials to a file                    |                                                            |

</details>

### More about search

- `-c` or `--category` can be used to limit search results to certain categories.
  - Available categories are "album", "artist", "playlist", "track", "show" and "episode".
  - You can search in multiple categories at once
- You can also narrow down results by using field filters in search queries
  - Currently available filters are album, artist, track, year, upc, tag:hipster, tag:new, isrc, and genre.
  - Available filters are album, artist, track, year, upc, tag:hipster, tag:new, isrc, and genre.
  - The artist and year filters can be used while searching albums, artists and tracks. You can filter on a single year or a range (e.g. 1970-1982).
  - The album filter can be used while searching albums and tracks.
  - The genre filter can be used while searching artists and tracks.
  - The isrc and track filters can be used while searching tracks.
  - The upc, tag:new and tag:hipster filters can only be used while searching albums. The tag:new filter will return albums released in the past two weeks and tag:hipster can be used to show only albums in the lowest 10% of popularity.

## Usage as a library

Zotify can be used as a user-friendly library for saving music, podcasts, lyrics and metadata.

Here's a very simple example of downloading a track and its metadata:

```python
from zotify import Session

session = Session.from_userpass(username="username", password="password")
track = session.get_track("4cOdK2wGLETKBW3PvgPWqT")
output = track.create_output("./Music", "{artist} - {title}")

file = track.write_audio_stream(output)

file.write_metadata(track.metadata)
file.write_cover_art(track.get_cover_art())
```

## Contributing

Pull requests are always welcome, but if adding an entirely new feature we encourage you to create an issue proposing the feature first so we can ensure it's something that fits the scope of the project.

Zotify aims to be a comprehensive and user-friendly tool for downloading music and podcasts.
It is designed to be simple by default but offer a high level of configuration for users that want it.
All new contributions should follow this principle to keep the program consistent.

## Will my account get banned if I use this tool?

There have been no *confirmed* cases of accounts getting banned as a result of using Zotify.
However, it is still a possiblity and it is recommended you use Zotify with a burner account where possible.

Consider using [Exportify](https://watsonbox.github.io/exportify/) to keep backups of your playlists.

## Disclaimer

Using Zotify violates Sp‌otify user guidelines and may get your account suspended.

Zotify is intended to be used in compliance with DMCA, Section 1201, for educational, private and fair use, or any simlar laws in other regions.
Zotify contributors are not liable for damages caused by the use of this tool. See the [LICENSE](./LICENCE) file for more details.

---

**P.S.** This fork builds upon the excellent work of the original [Zotify project](https://github.com/zotify-dev/zotify) with performance optimizations and enhanced features for power users.
