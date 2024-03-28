

# Validation Report for Threat Analysis with Uptycs

| SDK Version       | Generation Time          | Command Line Arguments Provided |
| :---------------- | ------------------------ | ------------------------------- |
| 51.0.1.0.695 | 2024/03/28 22:20:20 | `verbose`: True, `cmd`: validate, `package`: . |

## Results
| **Severity** | **Count** |
| :----------- | --------- |
| Critical Issues:    | <span style="color:red"> 1 </span> |
| Warnings:           | <span style="color:orange"> 1 </span>  |
| Validations Passed: | <span style="color:green"> 36  </span>   |


## App Details
| Attribute | Value |
| --------- | ----- |
| `display_name` | Threat Analysis with Uptycs |
| `name` | threat_analysis_with_uptycs |
| `version` | 1.0.0 |
| `author` | Uptycs |
| `author_email` | kadirikumar@uptycs.com |
| `install_requires` | ['resilient-circuits>=51.0.1.0.0'] |
| `description` | Responds to threats everywhere across the cloud, endpoints, containers, and K8s systems |
| `long_description` | It is a robust extension that seamlessly integrates with the Uptycs platform to retrieve real-time alerts data and analyze potential security threats.     This integration empowers security teams to proactively monitor, analyze, and respond to security incidents within their organization's IT infrastructure, ensuring timely detection and mitigation of threats. |
| `url` | https://www.uptycs.com |
| `entry_points` | {'resilient.circuits.configsection': 'C:\\Users\\kadirikumar\\Downloads\\QRADAR-SOAR-V1\\threat_analysis_with_uptycs\\threat_analysis_with_uptycs\\util\\config.py',<br> 'resilient.circuits.customize': 'C:\\Users\\kadirikumar\\Downloads\\QRADAR-SOAR-V1\\threat_analysis_with_uptycs\\threat_analysis_with_uptycs\\util\\customize.py',<br> 'resilient.circuits.selftest': 'C:\\Users\\kadirikumar\\Downloads\\QRADAR-SOAR-V1\\threat_analysis_with_uptycs\\threat_analysis_with_uptycs\\util\\selftest.py'} |
| `python_requires` | >=3.11 |
| `SOAR version` | 50.0.9097 |
| `Proxy support` | Proxies supported if running on AppHost>=1.6 |

---


## `setup.py` file validation
| Severity | Name | Description | Solution |
| --- | --- | --- | --- |

<span style="color:green">Success</span>


---


## Package files validation

### LICENSE
<span style="color:teal">INFO</span>: `LICENSE` file is valid

It is recommended to manually validate the license. Suggested formats: MIT, Apache, and BSD


### `MANIFEST.in`
<span style="color:green">Pass</span>


### `apikey_permissions.txt`
<span style="color:green">Pass</span>


### `Dockerfile, template match`
<span style="color:green">Pass</span>


### `Dockerfile, base image`
<span style="color:green">Pass</span>


### ``config.py``
<span style="color:green">Pass</span>


### ``customize.py``
<span style="color:green">Pass</span>


### `SOAR Scripts`
<span style="color:green">Pass</span>


### `README.md`
<span style="color:green">Pass</span>


### `app_logo.png`
<span style="color:green">Pass</span>


### `company_logo.png`
<span style="color:green">Pass</span>


### LICENSE
<span style="color:green">Pass</span>

 
---
 

## Payload samples validation

### `payload_samples\uptycs_api`
<span style="color:green">Pass</span>

 
---
 

## `resilient-circuits` selftest

<span style="color:green">Success</span>


---
 

## tox tests
<span style="color:red">CRITICAL</span>: 3 tests failed. Details:

	self = <test_funct_uptycs_api.TestUptycsApi object at 0x000001FA15F60390>
	
	    def test_function_definition(self):
	        """ Test that the package provides customization_data that defines the function """
	        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
	>       assert func is not None
	E       assert None is not None
	
	tests\test_funct_uptycs_api.py:48: AssertionError
	
	---
	
	self = <test_funct_uptycs_api.TestUptycsApi object at 0x000001FA14C2B5D0>
	circuits_app = <pytest_resilient_circuits.resilient_circuits_fixtures.ResilientCircuits object at 0x000001FA1638D410>
	mock_inputs = {`uptycs_api_endpoint`: `/`, `uptycs_api_method`: `GET`, `uptycs_api_payload`: `{}`}
	
	    @pytest.mark.parametrize("mock_inputs", [(mock_inputs_1)])
	    def test_domain_details(self, circuits_app, mock_inputs):
	        """ Test calling with sample values for the parameters """
	    
	        results = call_uptycs_api_function(circuits_app, mock_inputs)
	>       response = results[`content`]
	E       TypeError: `NoneType` object is not subscriptable
	
	tests\test_funct_uptycs_api.py:67: TypeError
	
	---
	
	self = <test_funct_uptycs_api.TestUptycsApi object at 0x000001FA1766EC50>
	circuits_app = <pytest_resilient_circuits.resilient_circuits_fixtures.ResilientCircuits object at 0x000001FA1638D410>
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

<span style="color:orange">WARNING</span>: Unsupported tox environment found in envlist in `tox.ini` file

Tests must be configured to run only with tox environments `py36` or greater



---
 

## Pylint Scan
<span style="color:teal">INFO</span>: Pylint scan passed with no errors

Run with `-v` to see the full pylint output



---
 

## Bandit Scan
<span style="color:teal">INFO</span>: Bandit scan passed with no issues

Run again with `-v` to see the full bandit output



---
 