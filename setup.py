from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='audioanalytics',
      version='0.1',
      description='A python package to simplify the process of performing basic exploratory audio analysis',
      #   url='http://github.com/storborg/funniest',
      #   author='Flying Circus',
      #   author_email='flyingcircus@example.com',
      #   license='MIT',
      include_package_data=True,
      package_data={
          'audioanalytics': ['models/model.h5', 'models/model.json']
      },
      packages=setuptools.find_packages(exclude=['tests']),
      #   packages=['audioanalytics'],
      #   package_dir={'audioanalytics': 'audiopipanalytics'},
      zip_safe=False,
      install_requires=[  # Add list of dependencies here
          #     "Django >= 1.1.1",
          #     "pytest",
          "librosa",
          "tensorflow",
          "numpy",
          "pandas",
          #   "glob",
          #   "os",
          "soundfile",
          "keras",
          "setuptools"
      ],
      )
