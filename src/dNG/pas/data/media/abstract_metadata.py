# -*- coding: utf-8 -*-
##j## BOF

"""
dNG.pas.data.media.AbstractMetadata
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

class AbstractMetadata(object):
#
	"""
Abstract metadata class for media content.

:author:     direct Netware Group
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: imaging
:since:      v0.1.00
:license:    http://www.direct-netware.de/redirect.py?licenses;gpl
             GNU General Public License 2
	"""

	def __init__(self, url, **kwargs):
	#
		"""
Constructor __init__(AbstractMetadata)

:param url: Metadata source URL

:since: v0.1.00
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
:since:  v0.1.00
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
:since:  v0.1.00
		"""

		return self.data.get("comment")
	#

	def get_copyright(self):
	#
		"""
Returns embedded copyright information if any.

:return: (str) Copyright information; None if undefined
:since:  v0.1.00
		"""

		return self.data.get("copyright")
	#

	def get_description(self):
	#
		"""
Returns an embedded description if any.

:return: (str) Image description; None if undefined
:since:  v0.1.00
		"""

		return self.data.get("description")
	#

	def _set(self, **kwargs):
	#
		"""
Sets values given as keyword arguments to this method.

:since: v0.1.00
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
:since:  v0.1.00
		"""

		def proxymethod(self): return self.data.get(key, default_value)
		return proxymethod
	#
#

##j## EOF