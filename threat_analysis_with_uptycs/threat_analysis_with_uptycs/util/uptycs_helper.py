""" Calls Uptycs API and returns result """

import logging
import time
import hashlib
import base64
import json
import requests

log = logging.getLogger(__name__)

def call_uptycs(options, method, endpoint, payload):
    """ Calls Uptycs public API """
    log.info("Endpoint: %s", endpoint)
    log.info("Method: %s", method)
    log.info("Payload: %s", payload)
    key=options.uptycs_api_key
    secret=options.uptycs_api_secret
    headers=get_api_headers(key, secret)
    # Uptycs Parameters
    domain = options.uptycs_domain
    domain_suffix = options.uptycs_domain_suffix
    customer_id = options.uptycs_customer_id
    url = f'https://{domain + domain_suffix}/public/api'
    url += f'/customers/{customer_id}{endpoint}'

    try:
        response = requests.request(method=method, url=url,
                                            headers=headers, data=payload, timeout=180)
        return response
    except Exception:
        log.debug('Error while calling uptycs API')
        return Exception



def get_api_headers(key, secret):
    """Function to calculate header parameters"""
    token = get_jwt_token(key, secret)
    auth = f'Bearer {token}'
    credentials = {'Authorization': auth}
    return credentials



# Functions to generate JWT Token

def custom_hmac_sha256(key, data):
    """HMAC SHA256 Encoder"""
    key_bytes = key.encode('utf-8') if isinstance(key, str) else key
    block_size = 64

    if len(key_bytes) > block_size:
        key_bytes = hashlib.sha256(key_bytes).digest()

    key_bytes = key_bytes.ljust(block_size, b'\0')

    ipad = b'\x36' * block_size
    opad = b'\x5C' * block_size

    inner_key = bytes(x ^ y for x, y in zip(key_bytes, ipad))
    outer_key = bytes(x ^ y for x, y in zip(key_bytes, opad))

    inner_hash = hashlib.sha256(inner_key + data).digest()
    final_hash = hashlib.sha256(outer_key + inner_hash).digest()

    return final_hash

def encode_base64(data):
    """Base64 Encoder"""
    return base64.urlsafe_b64encode(data).rstrip(b'=')


def generate_jwt(header, payload, key):
    """ Final Token Genartor"""
    encoded_header = encode_base64(json.dumps(header).encode('utf-8'))
    encoded_payload = encode_base64(json.dumps(payload).encode('utf-8'))

    signing_input = encoded_header + b'.' + encoded_payload
    signature = custom_hmac_sha256(key, signing_input)
    encoded_signature = encode_base64(signature)

    return encoded_header + b'.' + encoded_payload + b'.' + encoded_signature



def get_jwt_token(key, secret):
    """Entry point for JWT Token generation step"""
    exp = time.time() + 300
    header = {'alg': 'HS256', 'typ': 'JWT'}
    payload = {'iss': key, 'exp': exp}
    token = generate_jwt(header, payload, secret).decode()
    return token
