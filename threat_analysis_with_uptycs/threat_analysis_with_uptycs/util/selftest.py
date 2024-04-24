# -*- coding: utf-8 -*-

"""
Function implementation test.
"""

import logging
from threat_analysis_with_uptycs.util.uptycs_helper import call_uptycs

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("threat_analysis_with_uptycs", {})

    try:
        call_uptycs(options=app_configs, method='GET', endpoint='/', payload='{}')
    except Exception as uptycs_exception:
        log.error("Encountered Exception when calling API, Exception: %s", uptycs_exception)
        return {"status": "failure", "reason": uptycs_exception}
    return {"state": "success"}
