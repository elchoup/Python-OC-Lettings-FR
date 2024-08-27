import sys
import sentry_sdk


def handle_exception(exc_type, exc_value, exc_traceback):
    # Ignore KeyboardInterrupt to allow normal termination of the program
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    # Log the exception with Sentry
    sentry_sdk.capture_exception(exc_value)
    print(f"Exception captured: {exc_value}")
