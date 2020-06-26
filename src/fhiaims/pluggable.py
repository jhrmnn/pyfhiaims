# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import logging

log = logging.getLogger(__name__)


class Plugin:
    name = None

    def __call__(self, pluggable):
        pluggable.register_plugin(self._name, self)

    @property
    def _name(self):
        return self.name or self.__class__.__name__


class Pluggable:
    def __init__(self):
        self._plugins = {}

    def register_plugin(self, name, plugin):
        self._plugins[name] = plugin

    def run_plugins(self, func, *args):
        for plugin in self._plugins.values():
            try:
                getattr(plugin, func)(*args)
            except Exception:
                log.error(f"Error in plugin {plugin._name!r}")
                raise
