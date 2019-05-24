from distutils.core import setup

setup(
  name = 'MultiServer',         # How you named your package folder (MyLib)
  packages = ['MultiServer'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Server for your app needs',   # Give a short description about your library
  author = 'Yehoyada.s',                   # Type in your name
  author_email = 'hvuhsg6@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/hvuhsg',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/hvuhsg/MultiServer/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['Server', 'Easy', 'app'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          "cryptography >= 2.3.1",
          "rsa >= 4.0",
          "pymongo >= 3.7.1",
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)