"""All dynamical system classes.

Classes:
AdaptivePendulum - Inverted pendulum system for adaptive control
Pendulum - Inverted pendulum system
DoublePendulum - Double inverted pendulum system
system - Base class for dynamical systems
"""

from .adaptive_pendulum import AdaptivePendulum
from .pendulum import Pendulum
from .double_pendulum import DoublePendulum
