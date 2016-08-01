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
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
----------------------------------------------------------------------------
https://www.direct-netware.de/redirect?licenses;gpl
----------------------------------------------------------------------------
#echo(pasMediaVersion)#
#echo(__FILEPATH__)#
"""

from dNG.data.supports_mixin import SupportsMixin
from dNG.runtime.not_implemented_exception import NotImplementedException

class Abstract(SupportsMixin):
#
	"""
This abstract class defines methods to open a file and get metadata for it.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: media
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
	"""

	# pylint: disable=unused-argument

	def get_metadata(self):
	#
		"""
Returns the metadata for this URL.

:return: (object) Metadata object
:since:  v0.2.00
		"""

		raise NotImplementedException()
	#

	def open_url(self, url):
	#
		"""
Initializes an media instance for the given URL.

:param url: URL

:return: (bool) True on success
:since:  v0.2.00
		"""

		return False
	#

	def save(self):
	#
		"""
Saves the media instance using the defined constraints.

:since: v0.2.00
		"""

		raise NotImplementedException()
	#

	@staticmethod
	def is_mimetype_supported(mimetype):
	#
		"""
Returns true if the given mime type is supported.

:param mimetype: Mime type to check

:return: (bool) True if supported
:since:  v0.2.00
		"""

		return False
	#
#

##j## EOF