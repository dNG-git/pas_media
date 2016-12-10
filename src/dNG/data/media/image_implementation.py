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

# pylint: disable=import-error, no-name-in-module

from dNG.data.logging.log_line import LogLine
from dNG.data.settings import Settings

from .abstract_implementation import AbstractImplementation

class ImageImplementation(AbstractImplementation):
    """
"ImageImplementation" provides methods to load a configured implementation
for image handling and transformation.

:author:     direct Netware Group et al.
:copyright:  direct Netware Group - All rights reserved
:package:    pas
:subpackage: media
:since:      v0.2.00
:license:    https://www.direct-netware.de/redirect?licenses;gpl
             GNU General Public License 2
    """

    @staticmethod
    def _get_implementation_class_name():
        """
Returns the media implementation class name based on the configuration set.

:return: (str) Media implementation class name
:since:  v0.2.00
        """

        Settings.read_file("{0}/settings/pas_media.json".format(Settings.get("path_data")))

        _return = Settings.get("pas_media_image_implementation", "")
        if (_return == ""): LogLine.warning("Media image implementation class is not configured")

        return _return
    #
#
