import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (package.key, package.version) for package in installed_packages])
print(installed_packages_list)

import pip
from subprocess import call
for package in installed_packages_list:
    print("pip install --upgrade " + package[:package.find("==")])
    call("pip install --upgrade " + package[:package.find("==")], shell=True)
