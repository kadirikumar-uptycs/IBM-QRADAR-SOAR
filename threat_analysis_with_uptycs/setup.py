#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    version="1.1.0",
    license="MIT",
    author="Uptycs",
    author_email="kadirikumar@uptycs.com",
    url="https://www.uptycs.com",
    description="Responds to threats everywhere across the cloud, endpoints, containers, and K8s systems",
    long_description="""Uptycs harnesses rich data insights to achieve deeper contextual understanding, while our unified approach integrates structured telemetry, cloud-based analytics, and adherence to standards for seamless interoperability.

The QRadar SOAR extension by Uptycs offers a seamless integration with the Uptycs platform, enabling real-time retrieval and analysis of alerts data to bolster security efforts. This integration equips security teams with the capability to monitor, analyze, and respond to potential threats within their organization's IT infrastructure swiftly and effectively. Uptycs' comprehensive detection and response capabilities span across various environments, including cloud, endpoints, containers, and Kubernetes systems, ensuring robust protection against evolving security challenges and minimizing risks across the entire attack surface.

Key Capabilities of Uptycs Comprehensive Threat Detection and Response:
* Swiftly detects malicious activity on Linux workloads in the Cloud.
* Identifies potential malicious activity within the Cloud environment by ingesting and monitoring diverse cloud logs and searching for patterns of user/API activity to generate detections.
* Offers a detailed analysis including event timelines, user/API actions, and metadata to facilitate thorough investigation and response.
Provides container and Kubernetes-specific detections by correlating multiple events to identify potential threats.
* Protects macOS, Windows, and Linux endpoints by meticulously analyzing signal scores, YARA detections, and alert severity.

For more information, visit [https://www.uptycs.com/](https://www.uptycs.com/)""",
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
