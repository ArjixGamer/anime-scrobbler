from dataclasses import dataclass
from typing import List, Optional

from plexapi.video import Show
from anilist import MediaEntry


@dataclass()
class DownloadableQueue:
    shows_found_in_plex: List[Optional[Show]]
    shows_missing_in_plex: List[Optional[MediaEntry]]
    show_media_entry_in_plex: List[Optional[MediaEntry]]

    def contains_items(self):
        return self.shows_found_in_plex or self.shows_missing_in_plex or self.show_media_entry_in_plex
