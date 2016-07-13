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

from dNG.module.named_loader import NamedLoader
from dNG.runtime.not_implemented_class import NotImplementedClass
from dNG.runtime.not_implemented_exception import NotImplementedException

class AbstractImplementation(object):
#
	"""
"AbstractImplementation" provides methods to load a configured
implementation for media handling and transformation.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: media
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
	"""

	@classmethod
	def get_class(cls, is_not_implemented_class_aware = False):
	#
		"""
Returns an media implementation class based on the configuration set.

:param cls: Python class
:param is_not_implemented_class_aware: True to return
       "dNG.runtime.NotImplementedClass" instead of None

:return: (object) Media implementation class; None if not available
:since:  v0.2.00
		"""

		implementation_class_name = cls._get_implementation_class_name()

		_return = (None
		           if (implementation_class_name == "") else
		           NamedLoader.get_class("dNG.data.media.{0}".format(implementation_class_name))
		          )

		if (_return is None and is_not_implemented_class_aware): _return = NotImplementedClass

		return _return
	#

	@staticmethod
	def _get_implementation_class_name():
	#
		"""
Returns the media implementation class name based on the configuration set.

:return: (str) Media implementation class name
:since:  v0.2.00
		"""

		raise NotImplementedException()
	#

	@classmethod
	def get_instance(cls, *args, **kwargs):
	#
		"""
Returns an media implementation instance based on the configuration set.

:param cls: Python class

:return: (object) Media implementation instance
:since:  v0.2.00
		"""

		implementation_class = cls.get_class(True)
		return implementation_class(*args, **kwargs)
	#
#

##j## EOF