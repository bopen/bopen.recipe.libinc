
import os
import logging      

import zc.buildout

class Recipe:
    """zc.buildout recipe for parsing unix-config commands"""

    def __init__(self, buildout, name, options):
        self.options, self.name = options, name
        self.libraries = []
        self.library_dirs = []
        self.include_dirs = []

        log = logging.getLogger(self.name)

        for command in self.options.get('config-commands', '').splitlines():
            if command.strip() is '':
                continue
            command_output = os.popen(command).read().strip()
            log.info('%s -> %s' % (command, command_output))
            command_output_tokens = command_output.split()
            self.include_dirs += [option[2:] for option in command_output_tokens if option.startswith('-I')]
            self.library_dirs += [option[2:] for option in command_output_tokens if option.startswith('-L')]
            self.libraries += [option[2:] for option in command_output_tokens if option.startswith('-l')]

        self.options['cflags'] = ' '.join(['-I%s' % d for d in self.include_dirs])
        self.options['ldflags'] = ' '.join(['-L%s' % d for d in self.library_dirs]) + ' ' + \
            ' '.join(['-l%s' % n for n in self.libraries])
        self.options['include_dirs'] = str(self.include_dirs)
        self.options['library_dirs'] = str(self.library_dirs)
        self.options['libraries'] = str(self.libraries)

        log.info('''
        include_dirs: %(include_dirs)s
        library_dirs: %(library_dirs)s
        libraries: %(libraries)s
        cflags: %(cflags)s
        ldflags: %(ldflags)s
        ''' % self.options)

    def update(self):
        pass

    def install(self):
        return ()
