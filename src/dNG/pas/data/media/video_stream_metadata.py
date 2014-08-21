# -*- coding: utf-8 -*-
##j## BOF

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
59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;gpl
----------------------------------------------------------------------------
#echo(pasMediaVersion)#
#echo(__FILEPATH__)#
"""

from .stream_metadata import StreamMetadata

class VideoStreamMetadata(StreamMetadata):
#
	"""
This class provides methods for video stream metadata.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: imaging
:since:      v0.1.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
	"""

	instance_class = "dNG.pas.data.media.VideoStreamMetadata"
	"""
The qualified name of the class.
	"""

	get_bitrate = StreamMetadata._wrap_getter("bitrate")
	"""
Returns the bitrate.

:return: (str) Video bitrate; None if unknown
:since:  v0.1.00
	"""

	get_bpp = StreamMetadata._wrap_getter("bpp")
	"""
Returns the image bits per pixel value.

:return: (int) Image bpp
:since:  v0.1.00
	"""

	get_framerate = StreamMetadata._wrap_getter("framerate")
	"""
Returns the framerate.

:return: (str) Video framerate; None if unknown
:since:  v0.1.00
	"""

	get_height = StreamMetadata._wrap_getter("height")
	"""
Returns the video height.

:return: (int) Video stream height
:since:  v0.1.00
	"""

	get_width = StreamMetadata._wrap_getter("width")
	"""
Returns the video width.

:return: (int) Video stream width
:since:  v0.1.00
	"""
#

##j## EOF