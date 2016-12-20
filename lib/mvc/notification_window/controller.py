"""Controller of the notification window."""

from lib.mvc.bases import ControllerBase
from lib.mvc.notification_window.model import NotificationWindowModel, NotificationWindowView
from lib.exception_feedback import add_default_exception_handling

class NotificationWindowController(ControllerBase):
    def __init__(self, app):
        super().__init__()

        self.view.initialize()