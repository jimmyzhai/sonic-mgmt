from os import path
_TEMPLATE_DIR = "dash/templates"
TEMPLATE_DIR = path.abspath(_TEMPLATE_DIR)
# Constants used for generating dash configs
ENI = "eni"
LOOPBACK_IP = "loopback_ip"
VM_VNI = "vm_vni"
VNET1_VNI = "vnet1_vni"
VNET1_NAME = "vnet1_name"
VNET2_VNI = "vnet2_vni"
VNET2_NAME = "vnet2_name"
REMOTE_CA_IP = "remote_ca_ip"
LOCAL_CA_IP = "local_ca_ip"
REMOTE_PA_IP = "remote_pa_ip"
LOCAL_PA_IP = "local_pa_ip"
REMOTE_ENI_MAC = "remote_eni_mac"
LOCAL_ENI_MAC = "local_eni_mac"
DUT_MAC = "dut_mac"
REMOTE_PTF_MAC = "remote_ptf_mac"
LOCAL_PTF_MAC = "local_ptf_mac"
REMOTE_CA_PREFIX = "remote_ca_prefix"
REMOTE_PA_PREFIX = "remote_pa_prefix"
LOCAL_PTF_INTF = "local_ptf_intf"
REMOTE_PTF_INTF = "remote_ptf_intf"
ROUTING_TYPE = "routing_type"
ROUTING_ACTION_TYPE = "routing_action_type"
LOOKUP_OVERLAY_IP = "lookup_overlay_ip"
OUTBOUND_ROUTING_GROUP = "outbound_routing_group"
# For ACL
ACL_GROUP = "acl_group"
ACL_STAGE = "acl_stage"
ACL_RULE = "acl_rule"
IP_VERSION = "ip_version"
ACL_PRIORITY = "priority"
ACL_ACTION = "action"
ACL_TERMINATING = "terminating"
ACL_SRC_ADDR = "src_addr"
ACL_DST_ADDR = "dst_addr"
ACL_SRC_PORT = "src_port"
ACL_DST_PORT = "dst_port"
ACL_SRC_TAG = "src_tag"
ACL_DST_TAG = "dst_tag"
ACL_PROTOCOL = "protocol"
ACL_TAG = "acl_tag"
ACL_PREFIX_LIST = "prefix_list"
