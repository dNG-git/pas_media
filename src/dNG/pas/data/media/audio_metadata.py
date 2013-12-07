# -*- coding: utf-8 -*-
##j## BOF

"""
dNG.pas.data.media.AudioMetadata
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

from os import path

try: from urllib.parse import unquote
except ImportError: from urllib import unquote

from .audio_stream_metadata import AudioStreamMetadata

class AudioMetadata(AudioStreamMetadata):
#
	"""
This class provides methods for audio metadata.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: imaging
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;gpl
             GNU General Public License 2
	"""

	instance_class = "dNG.pas.data.media.AudioMetadata"
	"""
The qualified name of the class.
	"""

	get_album = AudioStreamMetadata._wrap_getter("album")
	"""
Returns the album name if any.

:return: (str) Album name; None if undefined
:since:  v0.1.00
	"""

	get_album_artist = AudioStreamMetadata._wrap_getter("album_artist")
	"""
Returns the album artist if any.

:return: (str) Album artist; None if undefined
:since:  v0.1.00
	"""

	get_artist = AudioStreamMetadata._wrap_getter("artist")
	"""
Returns the artist if any.

:return: (str) Artist; None if undefined
:since:  v0.1.00
	"""

	get_genre = AudioStreamMetadata._wrap_getter("genre")
	"""
Returns the genre if set.

:return: (int) Genre; None if undefined
:since:  v0.1.00
	"""

	get_length = AudioStreamMetadata._wrap_getter("length")
	"""
Returns the audio length.

:return: (int) Audio length
:since:  v0.1.00
	"""

	def get_title(self):
	#
		"""
Returns the title.

:return: (str) Title
:since:  v0.1.00
		"""

		_return = self.data.get("title")
		if (_return == None): _return = unquote(path.splitext(path.split(self.url)[1])[0])
		return _return
	#

	get_track = AudioStreamMetadata._wrap_getter("track")
	"""
Returns the track number if any.

:return: (int) Track number; None if undefined
:since:  v0.1.00
	"""
#

##j## EOF