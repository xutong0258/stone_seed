import os
import sys
# 添加项目根目录到路径
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from base import fileOP


if __name__ == '__main__':
    result_dict = {}
    result_yaml_file = 'result.yaml'
    result_dict['Ndis_netadapter1_name'] = 'Microsoft Wi-Fi Direct Virtual Adapter #2'
    result_dict['Ndis_netadapter12name'] = 'Realtek 8821CE Wireless LAN 802.11ac PCI-E NIC'
    fileOP.dump_file(result_yaml_file, result_dict)
    pass
