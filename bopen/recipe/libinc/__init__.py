
import os
import logging      

import zc.buildout

class Recipe:
    """zc.buildout recipe for parsing unix-config commands"""

    def __init__(self, buildout, name, options):
        libraries = []
        library_dirs = []
        include_dirs = []

        log = logging.getLogger(name)

        for command in self.options.get('flags-command', '').splitlines():
            if command.strip() is '':
                continue
            command_output = os.popen(command).read().strip()
            log.info('%s -> %s' % (command, command_output))

            command_output_tokens = command_output.split()
            include_dirs += [option[2:] for option in command_output_tokens if option.startswith('-I')]
            library_dirs += [option[2:] for option in command_output_tokens if option.startswith('-L')]
            libraries += [option[2:] for option in command_output_tokens if option.startswith('-l')]

        self.options['cflags'] = ' '.join(['-I%s' % d for d in self.include_dirs])
        self.options['ldflags'] = ' '.join(['-L%s' % d for d in self.library_dirs]) + ' ' + \
            ' '.join(['-l%s' % n for n in self.libraries])
        self.options['include_dirs'] = str(self.include_dirs)
        self.options['include-dirs'] = ' '.join(self.include_dirs)
        self.options['library_dirs'] = str(self.library_dirs)
        self.options['library-dirs'] = ' '.join(self.library_dirs)
        self.options['libraries'] = str(self.libraries)
        log_template = \
'''
    include_dirs: %(include_dirs)s
    library_dirs: %(library_dirs)s
    libraries: %(libraries)s
    cflags: %(cflags)s
    ldflags: %(ldflags)s
''' 
        log.info(log_template % self.options)


    def update(self):
        pass

    def install(self):
        return ()
