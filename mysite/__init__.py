# sportecontact/__init__.py

# Import necessary modules and packages
from . import users
from . import events
from . import utils

# Initialize any necessary configurations
DEBUG_MODE = True
DATABASE_URL = "sqlite://localhost/sportecontact.db"

# Set up logging
import logging
logging.basicConfig(level=logging.DEBUG if DEBUG_MODE else logging.INFO)

# Provide convenience functions or variables
DEFAULT_EVENT_LIMIT = 10
DEFAULT_USER_ROLE = 'member'

# Import commonly used classes or functions
from .users import User, UserManager
from .events import Event, EventManager