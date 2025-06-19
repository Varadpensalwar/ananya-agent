class SpeechToTextError(Exception):
    """Custom exception for Speech-to-text conversion errors."""

    pass


class TextToSpeechError(Exception):
    """Custom exception for Text-to-speech conversion errors."""

    pass


class TextToImageError(Exception):
    """Custom exception for Text-to-image generation errors."""

    pass


class ImageToTextError(Exception):
    """Custom exception for Image-to-text conversion errors."""

    pass
