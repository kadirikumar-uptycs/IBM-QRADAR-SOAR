# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.1.0.695

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l threat-analysis-with-uptycs
    resilient-circuits selftest --print-env -l threat-analysis-with-uptycs

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("threat_analysis_with_uptycs", {})
    print(app_configs)

    return {
        "state": "success",
        "reason": None
    }
