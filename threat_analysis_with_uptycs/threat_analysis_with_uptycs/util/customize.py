# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v51.0.1.0.695

"""Generate the SOAR customizations required for threat_analysis_with_uptycs"""

import base64
import os
import io
try:
    from resilient import ImportDefinition
except ImportError:
    # Support Apps running on resilient-circuits < v35.0.195
    from resilient_circuits.util import ImportDefinition

RES_FILE = "data/export.res"


def codegen_reload_data():
    """
    Parameters required reload codegen for the threat_analysis_with_uptycs package
    """
    return {
        "package": u"threat_analysis_with_uptycs",
        "message_destinations": [
            u"fn_uptycs_api"
        ],
        "functions": [
            u"uptycs_api"
        ],
        "workflows": [],
        "actions": [],
        "incident_fields": [
            u"uptycs_alert_assetid",
            u"uptycs_alert_code",
            u"uptycs_alert_description",
            u"uptycs_alert_gateway",
            u"uptycs_alert_hostname",
            u"uptycs_alert_id",
            u"uptycs_alert_key",
            u"uptycs_alert_rulename",
            u"uptycs_alert_severity",
            u"uptycs_alert_time",
            u"uptycs_alert_url",
            u"uptycs_alert_value",
            u"uptycs_detection_alerts",
            u"uptycs_detection_assethostname",
            u"uptycs_detection_attackmatrix",
            u"uptycs_detection_events",
            u"uptycs_detection_id",
            u"uptycs_detection_iscontainer",
            u"uptycs_detection_name",
            u"uptycs_detection_score",
            u"uptycs_detection_url",
            u"uptycs_is_alert_data",
            u"uptycs_is_detection_complete",
            u"uptycs_is_detection_data"
        ],
        "incident_artifact_types": [],
        "incident_types": [],
        "datatables": [
            u"uptycs_alerts_db",
            u"uptycs_alerts_of_detections_db",
            u"uptycs_detections_db"
        ],
        "automatic_tasks": [],
        "scripts": [
            u"JSON TO HTML (RICH TEXT)"
        ],
        "playbooks": [
            u"threat_analysis_with_uptycs_alerts_pb",
            u"threat_analysis_with_uptycs_detections_pb"
        ]
    }


def customization_data(client=None):
    """
    Returns a Generator of ImportDefinitions (Customizations).
    Install them using `resilient-circuits customize`

    IBM SOAR Platform Version: 50.0.9097

    Contents:
    - Message Destinations:
        - fn_uptycs_api
    - Functions:
        - uptycs_api
    - Playbooks:
        - threat_analysis_with_uptycs_alerts_pb
        - threat_analysis_with_uptycs_detections_pb
    - Incident Fields:
        - uptycs_alert_assetid
        - uptycs_alert_code
        - uptycs_alert_description
        - uptycs_alert_gateway
        - uptycs_alert_hostname
        - uptycs_alert_id
        - uptycs_alert_key
        - uptycs_alert_rulename
        - uptycs_alert_severity
        - uptycs_alert_time
        - uptycs_alert_url
        - uptycs_alert_value
        - uptycs_detection_alerts
        - uptycs_detection_assethostname
        - uptycs_detection_attackmatrix
        - uptycs_detection_events
        - uptycs_detection_id
        - uptycs_detection_iscontainer
        - uptycs_detection_name
        - uptycs_detection_score
        - uptycs_detection_url
        - uptycs_is_alert_data
        - uptycs_is_detection_complete
        - uptycs_is_detection_data
    - Data Tables:
        - uptycs_alerts_db
        - uptycs_alerts_of_detections_db
        - uptycs_detections_db
    - Scripts:
        - JSON TO HTML (RICH TEXT)
    """

    res_file = os.path.join(os.path.dirname(__file__), RES_FILE)
    if not os.path.isfile(res_file):
        raise FileNotFoundError("{} not found".format(RES_FILE))

    with io.open(res_file, mode='rt') as f:
        b64_data = base64.b64encode(f.read().encode('utf-8'))
        yield ImportDefinition(b64_data)