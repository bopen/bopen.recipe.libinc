
import os
import logging      

import zc.buildout

class LibInc:
    """zc.buildout recipe for parsing unix-config commands"""

    def __init__(self, buildout, name, options):
        libraries = []
        library_dirs = []
        include_dirs = []

        log = logging.getLogger(name)

        for command in options.get('flags-command', '').splitlines():
            if command.strip() is '':
                continue
            command_output = os.popen(command).read().strip()
            log.info('%s -> %s' % (command, command_output))

            command_output_tokens = command_output.split()
            include_dirs += [option[2:] for option in command_output_tokens if option.startswith('-I')]
            library_dirs += [option[2:] for option in command_output_tokens if option.startswith('-L')]
            libraries += [option[2:] for option in command_output_tokens if option.startswith('-l')]

        options['cflags'] = ' '.join(['-I%s' % d for d in include_dirs])
        options['ldflags'] = ' '.join(['-L%s' % d for d in library_dirs]) + ' ' + \
            ' '.join(['-l%s' % n for n in libraries])
        options['include_dirs'] = str(include_dirs)
        options['include-dirs'] = ' '.join(include_dirs)
        options['library_dirs'] = str(library_dirs)
        options['library-dirs'] = ' '.join(library_dirs)
        options['libraries'] = str(libraries)
        log_template = \
'''
    include_dirs: %(include_dirs)s
    library_dirs: %(library_dirs)s
    libraries: %(libraries)s
    cflags: %(cflags)s
    ldflags: %(ldflags)s
''' 
        log.info(log_template % options)
        self.options, self.name = options, name 

    def update(self):
        pass

    def install(self):
        for setup_cfg in self.options.get('setup-cfg', '').split():
            source_file = open(setup_cfg)
            source = source_file.read()
            source_file.close()
            target = [line for line in source.splitlines() if line.find('libraries') < 0]
            target += ['libraries=%s' % self.options['libraries']]
            target_file = open(setup_cfg, 'w')
            target_file.writelines(target)
            target_file.close()
            print source
            print target
        return ()
