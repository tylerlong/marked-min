import re
from subprocess import Popen, PIPE
from fabric.api import local


def update():
    local('rm marked.min.js')
    output = Popen(["bower", "info", "marked"], stdout = PIPE).communicate()[0]
    latest_version = re.findall(r"version: '(\d+\.\d+\.\d+)',", output)[0]
    local('wget https://github.com/chjj/marked/archive/v{0}.zip'.format(latest_version))
    local('unzip v{0}.zip && rm v{0}.zip'.format(latest_version))
    local('uglifyjs marked-{0}/lib/marked.js --comments="/Copyright/" --mangle --compress > marked.min.js'.format(latest_version))
    local('rm -rf marked-{0}'.format(latest_version))
    print 'latest version: {0}'.format(latest_version)
