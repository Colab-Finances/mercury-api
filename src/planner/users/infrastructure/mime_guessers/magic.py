from mimetypes import guess_extension
from typing import Optional

from kink import inject
from magic import from_buffer  # type: ignore[import-not-found]

from src.planner.users.domain.mime_guesser import MimeGuesser


@inject(use_factory=True, alias=MimeGuesser)
class MagicMimeGuesser:
    def extension(self, file: bytes) -> Optional[str]:
        content_type = from_buffer(file, mime=True)
        return guess_extension(content_type)
