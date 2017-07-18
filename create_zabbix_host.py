#!/usr/bin/python
#coding:utf8
from pyzabbix import ZabbixAPI
zapi = ZabbixAPI('http://update.winupon.com/zabbix/')
zapi.login('shenzm', 'shenzm')

def create_zabbix_hostgroup(group_name):
    r = zapi.do_request(method='hostgroup.create', params={'name': group_name})
    return r['result']['groupids']

def create_zabbix_host(hosts, ips, group_name):
    groupid = create_zabbix_hostgroup(group_name)
    for i in range(len(hosts)):
        host_params = {'groups': [{'groupid': int(groupid)}],
            'host': hosts[i],
            'proxy_hostid': '11131',
            'interfaces': [{'dns': '',
                'ip': ips[i],
                'main': 1,
                'port': '10050',
                'type': 1,
                'useip': 1}],
            'templates': [{'templateid': '10001'}]}
        r = zapi.do_request(method='host.create', params=host_params)
        print r


if __name__ == '__main__':
    hosts = ['sc_phy_etohdb1', 'sc_phy_etohdb2', 'sc_phy_etohhisdb1', 'sc_phy_etohhisdb2', 'sc_phy_etoh_s_db', 'HeJiaoYu_APP_L09',
        'HeJiaoYu_APP_L10', 'HeJiaoYu_APP_L11', 'HeJiaoYu_APP_L12', 'HeJiaoYu_APP_L13', 'HeJiaoYu_APP_L14', 'HeJiaoYu_APP_L15',
        'HeJiaoYu_APP_L16', 'HeJiaoYu_Monitor_L01', 'HeJiaoYu_FILE_L01', 'HeJiaoYu_FILE_L02', 'HeJiaoYu_backup_L01']
    ips = ['10.102.51.38', '10.102.51.39', '10.102.51.232', '10.102.51.233', '10.102.51.234', '10.102.43.180', '10.102.43.181',
        '10.102.43.182', '10.102.43.183', '10.102.43.184', '10.102.43.185', '10.102.43.186', '10.102.43.187', '10.102.43.188',
        '10.102.43.189', '10.102.43.190', '10.102.43.127']
    create_zabbix_host(hosts, ips, groupname)
