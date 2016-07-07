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

from dNG.data.binary import Binary
from dNG.data.json_resource import JsonResource
from dNG.module.named_loader import NamedLoader
from dNG.runtime.value_exception import ValueException

class AbstractMetadata(object):
#
	"""
Abstract metadata class for media content.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: media
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
	"""

	JSON_VERSION = 1
	"""
Metadata version for incompatible changes
	"""

	instance_class = None
	"""
The qualified name of the class.
	"""

	def __init__(self, url, **kwargs):
	#
		"""
Constructor __init__(AbstractMetadata)

:param url: Metadata source URL

:since: v0.2.00
		"""

		self.data = { }
		"""
Metadata dict
		"""
		self.url = url
		"""
Metadata source URL
		"""

		self._set(**kwargs)
	#

	def get(self, *args):
	#
		"""
Return the requested values.

:return: (dict) Requested values
:since:  v0.2.00
		"""

		_return = { }

		for key in args: _return[key] = self.data.get(key)

		return _return
	#

	def get_comment(self):
	#
		"""
Returns an embedded comment if any.

:return: (str) Comment; None if undefined
:since:  v0.2.00
		"""

		return self.data.get("comment")
	#

	def get_copyright(self):
	#
		"""
Returns embedded copyright information if any.

:return: (str) Copyright information; None if undefined
:since:  v0.2.00
		"""

		return self.data.get("copyright")
	#

	def get_description(self):
	#
		"""
Returns an embedded description if any.

:return: (str) Description; None if undefined
:since:  v0.2.00
		"""

		return self.data.get("description")
	#

	def get_json(self):
	#
		"""
Returns a JSON representation of the metadata.

:return: (str) JSON encoded metadata
:since:  v0.2.00
		"""

		data = self._get_json_data()
		data['_meta_version'] = AbstractMetadata.JSON_VERSION
		data['_meta_url'] = self.url

		return JsonResource().data_to_json(data)
	#

	def _get_json_data(self):
	#
		"""
Returns a dict containing all JSON metadata.

:return: (dict) JSON metadata for export
:since:  v0.2.00
		"""

		if (self.__class__.instance_class is None): raise ValueException("The qualified name is not defined.")

		_return = self.data.copy()
		_return['_py_class'] = self.__class__.instance_class

		return _return
	#

	def get_mimeclass(self):
	#
		"""
Returns the mime class.

:return: (str) Mime class
:since:  v0.2.00
		"""

		return self.data.get("mimeclass")
	#

	def get_mimetype(self):
	#
		"""
Returns the mime type.

:return: (str) Mime type
:since:  v0.2.00
		"""

		return self.data.get("mimetype")
	#

	def get_url(self):
	#
		"""
Returns the metadata source URL.

:return: (str) Metadata source URL
:since:  v0.2.00
		"""

		return self.url
	#

	def _load_json_data(self, data):
	#
		"""
Load metadata into this metadata object.

:return: (bool) True on success
:since:  v0.2.00
		"""

		# pylint: disable=star-args

		self.url = data['_meta_url']
		del(data['_meta_url'])

		self._set(**data)

		return True
	#

	def _set(self, **kwargs):
	#
		"""
Sets values given as keyword arguments to this method.

:since: v0.2.00
		"""

		self.data.update(kwargs)
	#

	@staticmethod
	def _wrap_getter(key, default_value = None):
	#
		"""
Wraps a "get*" method to return the given data value or alternatively the
given default one.

:param key: Key to create the "get*" method for
:param default_value: Default value if undefined

:return: (object) Proxy method
:since:  v0.2.00
		"""

		def proxymethod(self): return self.data.get(key, default_value)
		return proxymethod
	#

	@staticmethod
	def load_json(json):
	#
		"""
Load metadata previously exported with the "get_json()" method.

:param json: JSON encoded metadata

:return: (object) Metadata object; None if metadata is incompatible
:since:  v0.2.00
		"""

		json = Binary.str(json)
		data = (JsonResource().json_to_data(json) if (type(json) is str) else None)

		if (data is None): raise ValueException("Failed to decode JSON metadata")
		return (AbstractMetadata._load_instance_json_data(data) if (data.get("_meta_version") == AbstractMetadata.JSON_VERSION) else None)
	#

	@staticmethod
	def _load_instance_json_data(data, url = None):
	#
		"""
Load metadata into the correct instance.

:param data: Raw metadata dict

:return: (object) Metadata object; None if metadata is incompatible
:since:  v0.2.00
		"""

		# pylint: disable=protected-access

		_return = None

		if (("_meta_url" in data or url is not None) and "_py_class" in data):
		#
			_return = NamedLoader.get_instance(data['_py_class'], False, url = (data['_meta_url'] if (url is None) else url))
			if (not _return._load_json_data(data)): _return = None
		#

		return _return
	#
#

##j## EOF