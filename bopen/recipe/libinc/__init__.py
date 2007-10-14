
import os
import logging      

import zc.buildout

class Recipe:
    """zc.buildout recipe for parsing unix-config commands"""

    def __init__(self, buildout, name, options):
        self.options, self.name = options, name

    def update(self):
        pass

    def run(self, cmd):
        if os.system(cmd):
            log = logging.getLogger(self.name).error('Error executing command: %s' % cmd)
            raise zc.buildout.UserError('System error')

    def install(self):
        log = logging.getLogger(self.name)
        for config_command in self.options.get('config-commands', '').split():
            print config_command
            link_options = os.popen(config_command + ' --libs').read().split()
            library_dirs = [option[2:] for option in link_options if option.startswith('-L')]
            libraries = [option[2:] for option in link_options if option.startswith('-l')]
            print library_dirs, libraries
        try:
            pass
            #self.run('./configure --prefix=%s %s' % (self.options['prefix'], configure_options))
            #self.run(make_cmd)
            #self.run('%s %s' % (make_cmd, make_targets))
        except:
            log.error('Compilation error. The package is left as is at %s where '
                      'you can inspect what went wrong' % os.getcwd())
            raise
        return ()
