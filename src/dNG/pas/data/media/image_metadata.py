# -*- coding: utf-8 -*-
##j## BOF

"""
dNG.pas.data.media.ImageMetadata
"""
"""n// NOTE
----------------------------------------------------------------------------
direct PAS
Python Application Services
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?pas;media

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
http://www.direct-netware.de/redirect.py?licenses;gpl
----------------------------------------------------------------------------
#echo(pasMediaVersion)#
#echo(__FILEPATH__)#
----------------------------------------------------------------------------
NOTE_END //n"""

from .abstract_metadata import AbstractMetadata

class ImageMetadata(AbstractMetadata):
#
	"""
This class provides methods for image metadata.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: imaging
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;gpl
             GNU General Public License 2
	"""

	instance_class = "dNG.pas.data.media.ImageMetadata"
	"""
The qualified name of the class.
	"""

	get_artist = AbstractMetadata._wrap_getter("artist")
	"""
Returns an image embedded artist information if any.

:return: (str) Artist information; None if undefined
:since:  v0.1.00
	"""

	get_bpp = AbstractMetadata._wrap_getter("bpp")
	"""
Returns the image bits per pixel value.

:return: (int) Image bpp
:since:  v0.1.00
	"""

	get_height = AbstractMetadata._wrap_getter("height")
	"""
Returns the image height.

:return: (int) Image height
:since:  v0.1.00
	"""

	get_producer = AbstractMetadata._wrap_getter("producer")
	"""
Returns the image device or software producer for the image.

:return: (str) Mime type
:since:  v0.1.00
	"""

	get_width = AbstractMetadata._wrap_getter("width")
	"""
Returns the image width.

:return: (int) Image width
:since:  v0.1.00
	"""
#

##j## EOF