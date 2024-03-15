#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.1.0.695

from setuptools import setup, find_packages
import glob
import ntpath


def get_module_name(module_path):
    """
    Return the module name of the module path
    """
    return ntpath.split(module_path)[1].split(".")[0]


def snake_to_camel(word):
    """
    Convert a word from snake_case to CamelCase
    """
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


setup(
    name="threat_analysis_with_uptycs",
    display_name="Threat Analysis with Uptycs",
    version="1.0.0",
    license="MIT",
    author="Uptycs",
    author_email="kadirikumar@uptycs.com",
    url="https://www.uptycs.com",
    description="Responds to threats everywhere across the cloud, endpoints, containers, and K8s systems",
    long_description="""It is a robust extension that seamlessly integrates with the Uptycs platform to retrieve real-time alerts data and analyze potential security threats. 
    This integration empowers security teams to proactively monitor, analyze, and respond to security incidents within their organization's IT infrastructure, ensuring timely detection and mitigation of threats.""",
    install_requires=[
        "resilient-circuits>=51.0.1.0.0"
    ],
    python_requires='>=3.11',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "resilient.circuits.components": [
            # When setup.py is executed, loop through the .py files in the components directory and create the entry points.
            "{}FunctionComponent = threat_analysis_with_uptycs.components.{}:FunctionComponent".format(snake_to_camel(get_module_name(filename)), get_module_name(filename)) for filename in glob.glob("./threat_analysis_with_uptycs/components/[a-zA-Z]*.py")
        ]
        ,
        "resilient.circuits.configsection": ["gen_config = threat_analysis_with_uptycs.util.config:config_section_data"],
        "resilient.circuits.customize": ["customize = threat_analysis_with_uptycs.util.customize:customization_data"],
        "resilient.circuits.selftest": ["selftest = threat_analysis_with_uptycs.util.selftest:selftest_function"]
    }
)
