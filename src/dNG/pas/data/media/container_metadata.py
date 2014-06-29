# -*- coding: utf-8 -*-
##j## BOF

"""
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
"""

# pylint: disable=import-error,no-name-in-module

from os import path

try: from urllib.parse import unquote
except ImportError: from urllib import unquote

from .abstract_metadata import AbstractMetadata

class ContainerMetadata(AbstractMetadata):
#
	"""
This class provides methods for container metadata.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: imaging
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;gpl
             GNU General Public License 2
	"""

	instance_class = "dNG.pas.data.media.ContainerMetadata"
	"""
The qualified name of the class.
	"""

	def __init__(self, url, **kwargs):
	#
		"""
Constructor __init__(ContainerMetadata)

:since: v0.1.00
		"""

		AbstractMetadata.__init__(self, url, **kwargs)

		self.audio_streams = [ ]
		"""
List of audio streams
		"""
		self.other_streams = [ ]
		"""
List of other streams
		"""
		self.text_streams = [ ]
		"""
List of text streams
		"""
		self.video_streams = [ ]
		"""
List of video streams
		"""
	#

	get_length = AbstractMetadata._wrap_getter("length")
	"""
Returns the total length of the video or its container.

:return: (int) Container length
:since:  v0.1.00
	"""

	def get_audio_stream_codecs(self):
	#
		"""
Returns the audio codecs used as a indexed list of mime type notations.

:return: (list) List of audio codecs
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.audio_streams: _return.append(stream.get_codec())

		return _return
	#

	def get_audio_stream_mimetypes(self):
	#
		"""
Returns the mime-types of all audio streams as a indexed list.

:return: (list) List of mime-type strings
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.audio_streams: _return.append(stream.get_mimetype())

		return _return
	#

	def get_audio_streams(self, position = None):
	#
		"""
Returns a list of audio stream metadata or the audio stream metadata
identified with the given position.

:return: (mixed) List of objects or metadata object; None on error
:since:  v0.1.00
		"""

		if (position == None):
		#
			_return = [ ]
			for stream in self.audio_streams: _return.append(stream)
		#
		else: _return = (self.audio_streams[position] if (position < len(self.audio_streams)) else None)

		return _return
	#

	def get_audio_streams_count(self):
	#
		"""
Returns the number of audio streams in the file.

:return: (int) Number of audio streams
:since:  v0.1.00
		"""

		return len(self.audio_streams)
	#

	def _get_json_data(self):
	#
		"""
Returns a dict containing all JSON metadata.

:return: (dict) JSON metadata for export
:since:  v0.1.00
		"""

		# pylint: disable=protected-access

		_return = AbstractMetadata._get_json_data(self)

		_return['_audio_streams'] = [ ]
		for stream in self.audio_streams: _return['_audio_streams'].append(stream._get_json_data())

		_return['_other_streams'] = [ ]
		for stream in self.other_streams: _return['_other_streams'].append(stream._get_json_data())

		_return['_text_streams'] = [ ]
		for stream in self.text_streams: _return['_text_streams'].append(stream._get_json_data())

		_return['_video_streams'] = [ ]
		for stream in self.video_streams: _return['_video_streams'].append(stream._get_json_data())

		return _return
	#

	def get_other_stream_codecs(self):
	#
		"""
Returns the stream codecs used as a indexed list of mime type notations.

:return: (list) List of stream codecs
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.other_streams: _return.append(stream.get_codec())

		return _return
	#

	def get_other_stream_mimetypes(self):
	#
		"""
Returns the mime-types of all other streams as a indexed list.

:return: (list) List of mime-type strings
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.other_streams: _return.append(stream.get_mimetype())

		return _return
	#

	def get_other_streams(self, position = None):
	#
		"""
Returns a list of other stream metadata or the other stream metadata
identified with the given position.

:return: (mixed) List of objects or metadata object; None on error
:since:  v0.1.00
		"""

		if (position == None):
		#
			_return = [ ]
			for stream in self.other_streams: _return.append(stream)
		#
		else: _return = (self.other_streams[position] if (position < len(self.other_streams)) else None)

		return _return
	#

	def get_other_streams_count(self):
	#
		"""
Returns the number of other streams in the file.

:return: (int) Number of other streams
:since:  v0.1.00
		"""

		return len(self.other_streams)
	#

	def get_text_stream_codecs(self):
	#
		"""
Returns the text stream codecs used as a indexed list of mime type
notations.

:return: (list) List of text stream codecs
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.text_streams: _return.append(stream.get_codec())

		return _return
	#

	def get_text_stream_mimetypes(self):
	#
		"""
Returns the mime-types of all text streams as a indexed list.

:return: (list) List of mime-type strings
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.text_streams: _return.append(stream.get_mimetype())

		return _return
	#

	def get_text_streams(self, position = None):
	#
		"""
Returns a list of text stream metadata or the text stream metadata
identified with the given position.

:return: (mixed) List of objects or metadata object; None on error
:since:  v0.1.00
		"""

		if (position == None):
		#
			_return = [ ]
			for stream in self.text_streams: _return.append(stream)
		#
		else: _return = (self.text_streams[position] if (position < len(self.text_streams)) else None)

		return _return
	#

	def get_text_streams_count(self):
	#
		"""
Returns the number of text streams in the file.

:return: (int) Number of text streams
:since:  v0.1.00
		"""

		return len(self.text_streams)
	#

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

	def get_video_stream_codecs(self):
	#
		"""
Returns the video codecs used as a indexed list of mime type notations.

:return: (list) List of video codecs
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.video_streams: _return.append(stream.get_codec())

		return _return
	#

	def get_video_stream_mimetypes(self):
	#
		"""
Returns the mime-types of all video streams as a indexed list.

:return: (list) List of mime-type strings
:since:  v0.1.00
		"""

		_return = [ ]
		for stream in self.video_streams: _return.append(stream.get_mimetype())

		return _return
	#

	def get_video_streams(self, position = None):
	#
		"""
Returns a list of video stream metadata or the video stream metadata
identified with the given position.

:return: (mixed) List of objects or metadata object; None on error
:since:  v0.1.00
		"""

		if (position == None):
		#
			_return = [ ]
			for stream in self.video_streams: _return.append(stream)
		#
		else: _return = (self.video_streams[position] if (position < len(self.video_streams)) else None)

		return _return
	#

	def get_video_streams_count(self):
	#
		"""
Returns the number of video streams in the file.

:return: (int) Number of video streams
:since:  v0.1.00
		"""

		return len(self.video_streams)
	#

	def _load_json_data(self, data):
	#
		"""
Load metadata into this metadata object.

:return: (bool) True on success
:since:  v0.1.00
		"""

		if ("_audio_streams" in data and "_other_streams" in data and "_text_streams" in data and "_video_streams" in data):
		#
			self.audio_streams = [ ]
			for stream_data in data['_audio_streams']: self.audio_streams.append(ContainerMetadata._load_instance_json_data(stream_data, data['_meta_url']))
			del(data['_audio_streams'])

			self.other_streams = [ ]
			for stream_data in data['_other_streams']: self.other_streams.append(ContainerMetadata._load_instance_json_data(stream_data, data['_meta_url']))
			del(data['_other_streams'])

			self.text_streams = [ ]
			for stream_data in data['_text_streams']: self.text_streams.append(ContainerMetadata._load_instance_json_data(stream_data, data['_meta_url']))
			del(data['_text_streams'])

			self.video_streams = [ ]
			for stream_data in data['_video_streams']: self.video_streams.append(ContainerMetadata._load_instance_json_data(stream_data, data['_meta_url']))
			del(data['_video_streams'])

			_return = AbstractMetadata._load_json_data(self, data)
		#
		else: _return = False

		return _return
	#
#

##j## EOF