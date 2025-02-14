# -*- coding: utf-8 -*-

"""
Discord API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Discord API.

:copyright: (c) 2015-2019 Rapptz
:license: MIT, see LICENSE for more details.

"""

__title__ = 'discord'
__author__ = 'Rapptz'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2019 Rapptz'
__version__ = '1.2.2'

from collections import namedtuple
import logging

from .client import Client
from .appinfo import AppInfo
from .user import User, ClientUser, Profile
from .emoji import Emoji, PartialEmoji
from .activity import *
from .channel import *
from .guild import Guild, SystemChannelFlags
from .relationship import Relationship
from .member import Member, VoiceState
from .message import Message, Attachment
from .asset import Asset
from .errors import *
from .calls import CallMessage, GroupCall
from .permissions import Permissions, PermissionOverwrite
from .role import Role
from .file import File
from .colour import Color, Colour
from .invite import Invite, PartialInviteChannel, PartialInviteGuild
from .widget import Widget, WidgetMember, WidgetChannel
from .object import Object
from .reaction import Reaction
from . import utils, opus, abc, rtp
from .enums import *
from .embeds import Embed
from .shard import AutoShardedClient
from .player import *
from .reader import *
from .webhook import *
from .voice_client import VoiceClient
from .audit_logs import AuditLogChanges, AuditLogEntry, AuditLogDiff
from .raw_models import *
from .speakingstate import SpeakingState

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=1, minor=2, micro=2, releaselevel='final', serial=0)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
