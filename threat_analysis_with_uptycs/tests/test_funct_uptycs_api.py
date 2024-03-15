# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "threat_analysis_with_uptycs"
FUNCTION_NAME = "uptycs_api"

# Read the default configuration-data section from the package
config_data = """[threat_analysis_with_uptycs]
uptycs_domain = quality2
uptycs_domain_suffix = .uptycs.io
uptycs_customer_id = 049dad7d-94fc-4d78-9740-f55d81e0adfe
uptycs_api_key = O6FGHURJYMHV3LK4EK5IJZUI2QC4Q7G2
uptycs_api_secret = 471EOh2wWsZZw9w4inb0uc99zs8tSbrIGt+mBNanRGswRzEhRqQpMj5ASthcZ1zc"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_uptycs_api_function(circuits, function_params, timeout=10):

    # Create the submitTestFunction event
    evt = SubmitTestFunction("uptycs_api", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("uptycs_api_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestUptycsApi:
    """ Tests for the uptycs_api function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "uptycs_api_method": "GET",
        "uptycs_api_payload": "{}",
        "uptycs_api_endpoint": "/"
    }

    mock_inputs_2 = {
        "uptycs_api_method": "GET",
        "uptycs_api_payload": "{}",
        "uptycs_api_endpoint": "/assets/count"
    }

    @pytest.mark.parametrize("mock_inputs", [
        (mock_inputs_1),
        (mock_inputs_2)
    ])
    def test_success(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """

        results = call_uptycs_api_function(circuits_app, mock_inputs)
        assert(results)
