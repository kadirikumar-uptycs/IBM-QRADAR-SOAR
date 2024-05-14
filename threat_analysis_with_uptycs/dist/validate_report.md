# Validation Report for Threat Analysis with Uptycs

| SDK Version  | Generation Time      | Command Line Arguments Provided                      |
| :----------- | -------------------- | ---------------------------------------------------- |
| 51.0.1.0.695 | 2024/05/14 11:14:22 | `verbose`: True, `cmd`: validate, `package`: . |

## Results

| **Severity**  | **Count**                     |
| :------------------ | ----------------------------------- |
| Critical Issues:    | `<span style="color:red">` 1      |
| Warnings:           | `<span style="color:orange">` 1   |
| Validations Passed: | `<span style="color:green">` 36   |

## App Details

| Attribute            | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `display_name`     | Threat Analysis with Uptycs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `name`             | threat_analysis_with_uptycs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `version`          | 1.1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `author`           | Uptycs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `author_email`     | kadirikumar@uptycs.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `install_requires` | ['resilient-circuits>=51.0.1.0.0']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `description`      | Responds to threats everywhere across the cloud, endpoints, containers, and K8s systems                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `long_description` | Uptycs harnesses rich data insights to achieve deeper contextual understanding, while our unified approach integrates structured telemetry, cloud-based analytics, and adherence to standards for seamless interoperability.<br />The QRadar SOAR extension by Uptycs offers a seamless integration with the Uptycs platform, enabling real-time retrieval and analysis of alerts data to bolster security efforts. This integration equips security teams with the capability to monitor, analyze, and respond to potential threats within their organization's IT infrastructure swiftly and effectively. Uptycs' comprehensive detection and response capabilities span across various environments, including cloud, endpoints, containers, and Kubernetes systems, ensuring robust protection against evolving security challenges and minimizing risks across the entire attack surface.<br /><br />Key Capabilities of Uptycs Comprehensive Threat Detection and Response:<br />• Swiftly detects malicious activity on Linux workloads in the Cloud.<br />• Identifies potential malicious activity within the Cloud environment by ingesting and monitoring diverse cloud logs and searching for patterns of user/API activity to generate detections.<br />• Offers a detailed analysis including event timelines, user/API actions, and metadata to facilitate thorough investigation and response.<br />• Provides container and Kubernetes-specific detections by correlating multiple events to identify potential threats.<br />• Protects macOS, Windows, and Linux endpoints by meticulously analyzing signal scores, YARA detections, and alert severity.<br /><br />For more information, visit [https://www.uptycs.com/](https://www.uptycs.com/) |
| `url`              | https://www.uptycs.com                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `entry_points`     | {'resilient.circuits.configsection': 'C:\\Users\\kadirikumar\\Downloads\\QRADAR-SOAR-V1\\threat_analysis_with_uptycs\\threat_analysis_with_uptycs\\util\\config.py',`<br>` 'resilient.circuits.customize': 'C:\\Users\\kadirikumar\\Downloads\\QRADAR-SOAR-V1\\threat_analysis_with_uptycs\\threat_analysis_with_uptycs\\util\\customize.py',`<br>` 'resilient.circuits.selftest': 'C:\\Users\\kadirikumar\\Downloads\\QRADAR-SOAR-V1\\threat_analysis_with_uptycs\\threat_analysis_with_uptycs\\util\\selftest.py'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `python_requires`  | >=3.11                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `SOAR version`     | 50.0.9097                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Proxy support`    | Proxies supported if running on AppHost>=1.6                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

---

## `setup.py` file validation

| Severity | Name | Description | Solution |
| -------- | ---- | ----------- | -------- |

`<span style="color:green">`Success

---

## Package files validation

### LICENSE

`<span style="color:teal">`INFO: `LICENSE` file is valid

It is recommended to manually validate the license. Suggested formats: MIT, Apache, and BSD

### `MANIFEST.in`

`<span style="color:green">`Pass

### `apikey_permissions.txt`

`<span style="color:green">`Pass

### `Dockerfile, template match`

`<span style="color:green">`Pass

### `Dockerfile, base image`

`<span style="color:green">`Pass

### ``config.py``

`<span style="color:green">`Pass

### ``customize.py``

`<span style="color:green">`Pass

### `SOAR Scripts`

`<span style="color:green">`Pass

### `README.md`

`<span style="color:green">`Pass

### `app_logo.png`

`<span style="color:green">`Pass

### `company_logo.png`

`<span style="color:green">`Pass

### LICENSE

`<span style="color:green">`Pass

---

## Payload samples validation

### `payload_samples\uptycs_api`

`<span style="color:green">`Pass

---

## `resilient-circuits` selftest

`<span style="color:green">`Success

---

## tox tests

`<span style="color:red">`CRITICAL: 3 tests failed. Details:

    self = <test_funct_uptycs_api.TestUptycsApi object at 0x000001FC2182F5D0>

    def test_function_definition(self):
	        """ Test that the package provides customization_data that defines the function """
	        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
	>       assert func is not None
	E       assert None is not None

    tests\test_funct_uptycs_api.py:48: AssertionError

    ---

    self = <test_funct_uptycs_api.TestUptycsApi object at 0x000001FC21B590D0>
	circuits_app = <pytest_resilient_circuits.resilient_circuits_fixtures.ResilientCircuits object at 0x000001FC218082D0>
	mock_inputs = {`uptycs_api_endpoint`: `/`, `uptycs_api_method`: `GET`, `uptycs_api_payload`: `{}`}

    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_1)])
	    def test_domain_details(self, circuits_app, mock_inputs):
	        """ Test calling with sample values for the parameters """

    results = call_uptycs_api_function(circuits_app, mock_inputs)
	>       response = results[`content`]
	E       TypeError: `NoneType` object is not subscriptable

    tests\test_funct_uptycs_api.py:67: TypeError

    ---

    self = <test_funct_uptycs_api.TestUptycsApi object at 0x000001FC22D8A210>
	circuits_app = <pytest_resilient_circuits.resilient_circuits_fixtures.ResilientCircuits object at 0x000001FC218082D0>
	mock_inputs = {`uptycs_api_endpoint`: `/assets/count`, `uptycs_api_method`: `GET`, `uptycs_api_payload`: `{}`}

    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_2)])
	    def test_assets_count(self, circuits_app, mock_inputs):
	        """ Test with assets count API """

    results = call_uptycs_api_function(circuits_app, mock_inputs)
	>       response = results[`content`]
	E       TypeError: `NoneType` object is not subscriptable

    tests\test_funct_uptycs_api.py:81: TypeError

    ---

Run with the `-v` flag to see more information

`<span style="color:orange">`WARNING: Unsupported tox environment found in envlist in `tox.ini` file

Tests must be configured to run only with tox environments `py36` or greater

---

## Pylint Scan

`<span style="color:teal">`INFO: Pylint scan passed with no errors

Run with `-v` to see the full pylint output

---

## Bandit Scan

`<span style="color:teal">`INFO: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output

---
