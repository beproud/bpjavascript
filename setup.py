from setuptools import setup
import sys

tests_require = []

if sys.version_info < (3,):
    tests_require.append("unittest2")


setup(name="bpjavascript",
      packages=["beproud", "beproud.javascript"],
      namespace_packages=["beproud"],
      test_suite="beproud.javascript",
      tests_require=tests_require,
)
