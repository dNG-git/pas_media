# -*- coding: utf-8 -*-

"""
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
https://www.direct-netware.de/redirect?pas;media

The following license agreement remains valid unless any additions or
changes are being made by direct Netware Group in a written form.

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;gpl
----------------------------------------------------------------------------
#echo(pasMediaVersion)#
#echo(__FILEPATH__)#
"""

from .stream_metadata import StreamMetadata

class AudioStreamMetadata(StreamMetadata):
    """
This class provides methods for audio stream metadata.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: media
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
    """

    instance_class = "dNG.data.media.AudioStreamMetadata"
    """
The qualified name of the class.
    """

    get_bitrate = StreamMetadata._wrap_getter("bitrate")
    """
Returns the bitrate.

:return: (str) Audio bitrate; None if unknown
:since:  v0.2.00
    """

    get_bps = StreamMetadata._wrap_getter("bps")
    """
Returns the bits per sample.

:return: (str) Bits per sample; None if undefined
:since:  v0.2.00
    """

    get_channels = StreamMetadata._wrap_getter("channels")
    """
Returns the number of channels.

:return: (str) Number of channels; None if undefined
:since:  v0.2.00
    """

    get_sample_rate = StreamMetadata._wrap_getter("sample_rate")
    """
Returns the sample rate in Hz.

:return: (str) Sample rate; None if undefined
:since:  v0.2.00
    """
#
