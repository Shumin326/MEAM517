""" 
Reference: https://github.com/RussTedrake/underactuated/blob/master/scripts/setup/jupyter_setup.py

In Colab, add the following piece of code to the beginning of each script to install Drake if it's not installed yet: 
```
!curl -s https://raw.githubusercontent.com/mposa/MEAM517/hw2/colab_drake_setup.py > drake_setup.py
from drake_setup import setup
setup()
```
"""

import sys
import platform
from IPython import get_ipython

def setup():
    """Install drake (if necessary) and set up the path.

    On Google Colab:

    This will take a minute, but should only need to reinstall once every 12
    hours. Colab will ask you to "Reset all runtimes", say no to save yourself
    the reinstall.
    """

    # decrease the height of jupyter's output box
    from IPython.display import Javascript
    display(Javascript('''google.colab.output.setIframeHeight(0, true, {maxHeight: 100})'''))

    try:
        import pydrake
    except ImportError:
        if platform.system() == "Darwin":
            get_ipython().system(
                u"if [ ! -d '/opt/drake' ]; then curl -o drake.tar.gz https://drake-packages.csail.mit.edu/drake/continuous/drake-latest-mac.tar.gz && tar -xzf drake.tar.gz -C /opt && export HOMEBREW_CURL_RETRIES=4 && brew update && brew bundle --file=/opt/drake/share/drake/setup/Brewfile --no-lock; fi"  # noqa
            )
        elif platform.linux_distribution() == ("Ubuntu", "18.04", "bionic"):
            get_ipython().system(
                u"if [ ! -d '/opt/drake' ]; then curl -o drake.tar.gz https://drake-packages.csail.mit.edu/drake/continuous/drake-latest-bionic.tar.gz && tar -xzf drake.tar.gz -C /opt &&apt-get update -o APT::Acquire::Retries=4 -qq && apt-get install -o APT::Acquire::Retries=4 -o Dpkg::Use-Pty=0 -qy --no-install-recommends $(cat /opt/drake/share/drake/setup/packages-bionic.txt); fi"  # noqa
            )
        else:
            assert False, "Unsupported platform"
        v = sys.version_info
        sys.path.append("/opt/drake/lib/python{}.{}/site-packages".format(
            v.major, v.minor))

if __name__ == "__main__":
    setup()