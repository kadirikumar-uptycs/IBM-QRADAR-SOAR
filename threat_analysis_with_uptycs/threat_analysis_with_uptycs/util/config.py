# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.1.0.695

"""Generate a default configuration-file section for threat_analysis_with_uptycs"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for threat_analysis_with_uptycs when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = """
    [threat_analysis_with_uptycs]
    uptycs_domain = <domain_name_of_uptycs_stack>
    uptycs_domain_suffix = <domain_suffix_of_uptycs_stack>
    uptycs_customer_id = <uptycs_customer_id>
    uptycs_api_key = <key_value_of_uptycs_api_keys>
    uptycs_api_secret = <secret_value_of_uptycs_api_keys>
    """
    return config_data
