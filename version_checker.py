# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import json
import os

import bpy

from . import paths


def get_blender_version() -> str:
    """Get Blender version as string."""
    ver = bpy.app.version
    return '%i.%i.%i' % (ver[0], ver[1], ver[2])


def get_addon_version() -> str:
    """Get BlenderKit addon version as string."""
    import blenderkit
    ver = blenderkit.bl_info['version']
    return '%i.%i.%i' % (ver[0], ver[1], ver[2])


def compare_versions(module):
    try:
        ver_local = module.bl_info['version']
        ver_local_float = ver_local[0] + .01 * ver_local[1] + .0001 * ver_local[2]

        tempdir = paths.get_temp_dir()
        ver_filepath = os.path.join(tempdir, 'addon_version.json')
        with open(ver_filepath, 'r',encoding='utf-8') as s:
            data = json.load(s)

        ver_online = data['addonVersion2.8'].split('.')
        ver_online_float = int(ver_online[0]) + .01 * int(ver_online[1]) + .0001 * int(ver_online[2])

        # print('versions: installed-%s, online-%s' % (str(ver_local_float), str(ver_online_float)))
        if ver_online_float > ver_local_float:
            return True
    except:
        print("couldn't compare addon versions")
    return False

