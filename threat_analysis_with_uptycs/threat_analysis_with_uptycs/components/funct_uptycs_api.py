# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2024. All Rights Reserved.
# pylint: disable=unused-argument, too-many-locals, unspecified-encoding

"""AppFunction implementation"""

import json
import logging
from resilient_circuits import AppFunctionComponent, function, FunctionResult
from resilient_circuits import FunctionError, StatusMessage, handler
from resilient_lib import ResultPayload
from threat_analysis_with_uptycs.util.uptycs_helper import call_uptycs
# from resilient_lib import validate_fields

PACKAGE_NAME = "threat_analysis_with_uptycs"
FN_NAME = "uptycs_api"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'uptycs_api'"""

    def __init__(self, opts):
        super().__init__(opts, PACKAGE_NAME)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function(FN_NAME)
    def _uptycs_api_function(self, event, *args, **kwargs):
        """
        Function: provides functionality to call Uptycs public API
        Inputs:
            -   fn_inputs.uptycs_api_payload
            -   fn_inputs.uptycs_api_endpoint
            -   fn_inputs.uptycs_api_method
        """

        yield StatusMessage(f"Starting App Function: '{FN_NAME}'")
        log = logging.getLogger(__name__)
        try:
            yield StatusMessage(f"inputs : {kwargs}")
            method = kwargs.get("uptycs_api_method")
            endpoint = kwargs.get("uptycs_api_endpoint")
            payload = json.loads(kwargs.get("uptycs_api_payload"))

            log.info("Endpoint: %s", endpoint)
            log.info("Method: %s", method)
            log.info("Payload: %s", payload)

            result_payload_format = ResultPayload(PACKAGE_NAME, **kwargs)

            yield StatusMessage("Sending HTTP Request to Uptycs")
            # Api Call
            try:
                response = call_uptycs(options=self.options, method=method,
                                       endpoint=endpoint, payload=payload)
            except Exception as error:
                log.debug("Error while calling API : %s", error)
                raise FunctionError(f"Encountered an unexpected exception. \
                                    Exception Message: {error}") from error
            yield StatusMessage("Request sent to Uptycs successfully")
            yield StatusMessage(" Response recieved from Uptycs")
            # Results
            result_payload_format = result_payload_format.done(
                success=True,
                reason="Rechead Uptycs Successfully",
                content=response.json()
            )
            yield StatusMessage(f"Endpoint reached successfully and\
                                    returning results for App Function: '{FN_NAME}'")
            yield StatusMessage(f"Finished running App Function: '{FN_NAME}'")
            log.info("complete")
            yield FunctionResult(result_payload_format)
        except Exception:
            yield FunctionError()
