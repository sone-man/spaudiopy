import setuptools

setuptools.setup(name='spaudiopy',
                 version='0.1 alpha',
                 description='Spatial Audio Python Package',
                 url='https://github.com/chris-hld/spaudiopy',
                 author='Chris Hold',
                 author_email='Chris.Hold@mailbox.tu-berlin.de',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 package_data={'spaudiopy': ['t_designs_1_21.mat',
                                             'fliegeMaierNodes_1_30.mat'
                                             ]},
                 install_requires=[
                                   'numpy',
                                   'scipy',
                                   'pandas',
                                   'joblib',
                                   'matplotlib',
                                   'soundfile',
                                   'sounddevice',
                                   'resampy',
                                   'h5py',
                                   'quadpy'
                                   ],
                 platforms='any',
                 python_requires='>=3.6',
                 classifiers=[
                 "Development Status :: 3 - Alpha",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3 :: Only",
                 "Topic :: Scientific/Engineering",
                 ],
                 zip_safe=True,
                 )
