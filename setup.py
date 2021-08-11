# -*- coding: utf-8 -*-

# https://stackoverflow.com/questions/20288711/post-install-script-with-python-setuptools
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


class PreDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        check_call("python3 -m pip install -U jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html".split())
        # develop.run(self)

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        check_call("python3 -m pip install -U jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html".split())
        # install.run(self)


packages = \
['jaxtpu']

package_data = \
{'': ['*']}

# install_requires = \
# ['jax[tpu]>=0.2.18,<0.3.0',
#  'jaxlib==0.1.69',
#  'libtpu-nightly @ '
#  'https://storage.googleapis.com/cloud-tpu-tpuvm-artifacts/wheels/libtpu-nightly/libtpu_nightly-0.1.dev20210709-py3-none-any.whl']

setup_kwargs = {
    'name': 'jaxtpu',
    'version': '0.1.4',
    'description': 'A helper package to install the latest JAX on TPUs, along with all necessary dependencies (e.g. libtpu-nightly)',
    'long_description': "# jaxtpu\n\n> A helper package to install the latest JAX on TPUs, along with all necessary dependencies (e.g. libtpu-nightly)\n\nWARNING: This repo is in development. It was automatically generated with [mkpylib](https://github.com/shawwn/scrap/blob/master/mkpylib). If you're reading this message, it means that I use this repo for my own purposes right now. It might not do anything at all; the default functionality is `print('TODO')`.\n\nIf you really want to try it out, feel free. I recommend reading through the code and commit history to see if it does what you need, or [ask me](#contact) for status updates.\n\nStay tuned!\n\n## Install\n\n```\npython3 -m pip install -U jaxtpu\n```\n\n## Usage\n\n```py\nimport jaxtpu\n\nprint('TODO')\n```\n\n## License\n\nMIT\n\n## Contact\n\nA library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!\n\nMy Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.\n\n- Twitter: [@theshawwn](https://twitter.com/theshawwn)\n- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)\n- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)\n- Website: [shawwn.com](https://www.shawwn.com)\n\n",
    'long_description_content_type': 'text/markdown',
    'author': 'Shawn Presser',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shawwn/jaxtpu',
    'packages': packages,
    'package_data': package_data,
    # 'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
    'cmdclass': {
        'develop': PreDevelopCommand,
        'install': PreInstallCommand,
    },
}


setup(**setup_kwargs)
