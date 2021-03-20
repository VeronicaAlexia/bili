# (C) 2019-2021 lifegpc
# This file is part of bili.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from threading import Thread


def makeSureSendKill(d: dict):
    """确保已经给线程发送了kill"""
    for key in d:
        if not d[key]._stop:
            d[key].kill()


def makeSureAllClosed(d: dict):
    """所有进程是否已经全部退出"""
    for key in d:
        t = d[key]
        if isinstance(t, Thread):
            if t.isAlive:
                return False
    return True
