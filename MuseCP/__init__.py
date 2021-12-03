#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automation Library for Acurus Muse Processors
:copyright: (c) 2021 by Michael Kade
:license: GNU, see LICENSE for more details.
"""

# Set default logging handler to avoid "No handler found" warnings.
import logging

# Import MuseCP module
from .MuseCP import MuseProcessor

logging.getLogger(__name__).addHandler(logging.NullHandler())

__title__ = "muse"
__version__ = "1.0.0"
