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

from .abstract_metadata import AbstractMetadata

class StreamMetadata(AbstractMetadata):
#
	"""
This class provides methods for any stream metadata.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: media
:since:      v0.1.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
	"""

	instance_class = "dNG.pas.data.media.StreamMetadata"
	"""
The qualified name of the class.
	"""

	get_codec = AbstractMetadata._wrap_getter("codec")
	"""
Returns the stream codec used as mime type notation.

:return: (str) Stream codec
:since:  v0.1.00
	"""

	get_codec_profile = AbstractMetadata._wrap_getter("codec_profile")
	"""
Returns the stream codec profile.

:return: (str) Stream codec profile
:since:  v0.1.00
	"""
#

##j## EOF