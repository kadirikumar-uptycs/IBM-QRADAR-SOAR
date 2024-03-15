# -*- coding: utf-8 -*-
# (c) Copyright Uptycs 2023. All Rights Reserved
# pylint: disable=unused-argument, too-many-locals

"""AppFunction implementation"""

import json
import logging
from resilient_circuits import AppFunctionComponent, function, FunctionResult
from resilient_circuits import FunctionError, StatusMessage
from resilient_lib import validate_fields, ResultPayload
import requests
from threat_analysis_with_uptycs.util.uptycs_helper import get_api_headers

PACKAGE_NAME = "threat_analysis_with_uptycs"
FN_NAME = "uptycs_api"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'uptycs_api'"""

    def __init__(self, opts):
        super().__init__(opts, PACKAGE_NAME)

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
            # validating app_configs
            validate_fields([
                {"name": "uptycs_domain"},
                {"name": "uptycs_domain_suffix"},
                {"name": "uptycs_customer_id"},
                {"name": "uptycs_api_key"},
                {"name": "uptycs_api_secret"},
                ],
                self.app_configs)
            # calculate headers
            headers=get_api_headers(key=self.app_configs.uptycs_api_key,
                                    secret=self.app_configs.uptycs_api_secret)
            # Uptycs Parameters
            domain = self.app_configs.uptycs_domain
            domain_suffix = self.app_configs.uptycs_domain_suffix
            customer_id = self.app_configs.uptycs_customer_id
            url = f'https://{domain + domain_suffix}/public/api'
            url += f'/customers/{customer_id}{endpoint}'

            yield StatusMessage("Sending HTTP Request to Uptycs")
            # Api Call
            try:
                response = requests.request(method=method, url=url,
                                            headers=headers, data=payload, timeout=180)
            except Exception as error:
                log.debug("Error while calling API : %s", error)
                raise FunctionError(f"Encountered an unexpected exception. \
                                    Exception Message: {error}") from error
            yield StatusMessage("Request sent to Uptycs successfully")
            yield StatusMessage(" Data recieved from Uptycs")
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
