# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SystemInitSpecV5Global(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ip_version': 'str',
        'ntp_servers': 'list[str]',
        'is_internal_dns': 'bool',
        'dns_servers': 'list[str]',
        'syslog_servers': 'list[str]',
        'cluster_type': 'str',
        'cluster_vsan_prefix_length_ipv6': 'int',
        'cluster_vmotion_prefix_length_ipv6': 'int',
        'cluster_management_prefix_length_ipv6': 'int',
        'cluster_management_gateway_ipv6': 'str',
        'cluster_systemvm_netmask': 'str',
        'cluster_systemvm_gateway': 'str',
        'cluster_systemvm_prefix_length_ipv6': 'int',
        'cluster_systemvm_gateway_ipv6': 'str',
        'cluster_management_netmask': 'str',
        'cluster_management_gateway': 'str',
        'cluster_vsan_netmask': 'str',
        'cluster_vmotion_netmask': 'str',
        'cluster_witness_netmask': 'str',
        'cluster_witness_gateway': 'str',
        'top_level_domain': 'str',
        'ha_isolation_addresses': 'list[str]'
    }

    attribute_map = {
        'ip_version': 'ip_version',
        'ntp_servers': 'ntp_servers',
        'is_internal_dns': 'is_internal_dns',
        'dns_servers': 'dns_servers',
        'syslog_servers': 'syslog_servers',
        'cluster_type': 'cluster_type',
        'cluster_vsan_prefix_length_ipv6': 'cluster_vsan_prefix_length_ipv6',
        'cluster_vmotion_prefix_length_ipv6': 'cluster_vmotion_prefix_length_ipv6',
        'cluster_management_prefix_length_ipv6': 'cluster_management_prefix_length_ipv6',
        'cluster_management_gateway_ipv6': 'cluster_management_gateway_ipv6',
        'cluster_systemvm_netmask': 'cluster_systemvm_netmask',
        'cluster_systemvm_gateway': 'cluster_systemvm_gateway',
        'cluster_systemvm_prefix_length_ipv6': 'cluster_systemvm_prefix_length_ipv6',
        'cluster_systemvm_gateway_ipv6': 'cluster_systemvm_gateway_ipv6',
        'cluster_management_netmask': 'cluster_management_netmask',
        'cluster_management_gateway': 'cluster_management_gateway',
        'cluster_vsan_netmask': 'cluster_vsan_netmask',
        'cluster_vmotion_netmask': 'cluster_vmotion_netmask',
        'cluster_witness_netmask': 'cluster_witness_netmask',
        'cluster_witness_gateway': 'cluster_witness_gateway',
        'top_level_domain': 'top_level_domain',
        'ha_isolation_addresses': 'ha_isolation_addresses'
    }

    def __init__(self, ip_version=None, ntp_servers=None, is_internal_dns=None, dns_servers=None, syslog_servers=None, cluster_type=None, cluster_vsan_prefix_length_ipv6=None, cluster_vmotion_prefix_length_ipv6=None, cluster_management_prefix_length_ipv6=None, cluster_management_gateway_ipv6=None, cluster_systemvm_netmask=None, cluster_systemvm_gateway=None, cluster_systemvm_prefix_length_ipv6=None, cluster_systemvm_gateway_ipv6=None, cluster_management_netmask=None, cluster_management_gateway=None, cluster_vsan_netmask=None, cluster_vmotion_netmask=None, cluster_witness_netmask=None, cluster_witness_gateway=None, top_level_domain=None, ha_isolation_addresses=None):  # noqa: E501
        """SystemInitSpecV5Global - a model defined in Swagger"""  # noqa: E501
        self._ip_version = None
        self._ntp_servers = None
        self._is_internal_dns = None
        self._dns_servers = None
        self._syslog_servers = None
        self._cluster_type = None
        self._cluster_vsan_prefix_length_ipv6 = None
        self._cluster_vmotion_prefix_length_ipv6 = None
        self._cluster_management_prefix_length_ipv6 = None
        self._cluster_management_gateway_ipv6 = None
        self._cluster_systemvm_netmask = None
        self._cluster_systemvm_gateway = None
        self._cluster_systemvm_prefix_length_ipv6 = None
        self._cluster_systemvm_gateway_ipv6 = None
        self._cluster_management_netmask = None
        self._cluster_management_gateway = None
        self._cluster_vsan_netmask = None
        self._cluster_vmotion_netmask = None
        self._cluster_witness_netmask = None
        self._cluster_witness_gateway = None
        self._top_level_domain = None
        self._ha_isolation_addresses = None
        self.discriminator = None
        if ip_version is not None:
            self.ip_version = ip_version
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if is_internal_dns is not None:
            self.is_internal_dns = is_internal_dns
        if dns_servers is not None:
            self.dns_servers = dns_servers
        if syslog_servers is not None:
            self.syslog_servers = syslog_servers
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_vsan_prefix_length_ipv6 is not None:
            self.cluster_vsan_prefix_length_ipv6 = cluster_vsan_prefix_length_ipv6
        if cluster_vmotion_prefix_length_ipv6 is not None:
            self.cluster_vmotion_prefix_length_ipv6 = cluster_vmotion_prefix_length_ipv6
        if cluster_management_prefix_length_ipv6 is not None:
            self.cluster_management_prefix_length_ipv6 = cluster_management_prefix_length_ipv6
        if cluster_management_gateway_ipv6 is not None:
            self.cluster_management_gateway_ipv6 = cluster_management_gateway_ipv6
        if cluster_systemvm_netmask is not None:
            self.cluster_systemvm_netmask = cluster_systemvm_netmask
        if cluster_systemvm_gateway is not None:
            self.cluster_systemvm_gateway = cluster_systemvm_gateway
        if cluster_systemvm_prefix_length_ipv6 is not None:
            self.cluster_systemvm_prefix_length_ipv6 = cluster_systemvm_prefix_length_ipv6
        if cluster_systemvm_gateway_ipv6 is not None:
            self.cluster_systemvm_gateway_ipv6 = cluster_systemvm_gateway_ipv6
        if cluster_management_netmask is not None:
            self.cluster_management_netmask = cluster_management_netmask
        if cluster_management_gateway is not None:
            self.cluster_management_gateway = cluster_management_gateway
        if cluster_vsan_netmask is not None:
            self.cluster_vsan_netmask = cluster_vsan_netmask
        if cluster_vmotion_netmask is not None:
            self.cluster_vmotion_netmask = cluster_vmotion_netmask
        if cluster_witness_netmask is not None:
            self.cluster_witness_netmask = cluster_witness_netmask
        if cluster_witness_gateway is not None:
            self.cluster_witness_gateway = cluster_witness_gateway
        if top_level_domain is not None:
            self.top_level_domain = top_level_domain
        if ha_isolation_addresses is not None:
            self.ha_isolation_addresses = ha_isolation_addresses

    @property
    def ip_version(self):
        """Gets the ip_version of this SystemInitSpecV5Global.  # noqa: E501

        IPV4 is the default value. IPV6 and DUALSTACK are for internal use only.  # noqa: E501

        :return: The ip_version of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this SystemInitSpecV5Global.

        IPV4 is the default value. IPV6 and DUALSTACK are for internal use only.  # noqa: E501

        :param ip_version: The ip_version of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """
        allowed_values = ["IPV4", "IPV6", "DUALSTACK"]  # noqa: E501
        if ip_version not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_version` ({0}), must be one of {1}"  # noqa: E501
                .format(ip_version, allowed_values)
            )

        self._ip_version = ip_version

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this SystemInitSpecV5Global.  # noqa: E501

        Array of IP addresses for the NTP servers  # noqa: E501

        :return: The ntp_servers of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this SystemInitSpecV5Global.

        Array of IP addresses for the NTP servers  # noqa: E501

        :param ntp_servers: The ntp_servers of this SystemInitSpecV5Global.  # noqa: E501
        :type: list[str]
        """

        self._ntp_servers = ntp_servers

    @property
    def is_internal_dns(self):
        """Gets the is_internal_dns of this SystemInitSpecV5Global.  # noqa: E501

        Whether the DNS server is internal  # noqa: E501

        :return: The is_internal_dns of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: bool
        """
        return self._is_internal_dns

    @is_internal_dns.setter
    def is_internal_dns(self, is_internal_dns):
        """Sets the is_internal_dns of this SystemInitSpecV5Global.

        Whether the DNS server is internal  # noqa: E501

        :param is_internal_dns: The is_internal_dns of this SystemInitSpecV5Global.  # noqa: E501
        :type: bool
        """

        self._is_internal_dns = is_internal_dns

    @property
    def dns_servers(self):
        """Gets the dns_servers of this SystemInitSpecV5Global.  # noqa: E501

        Array of IP addresses for the DNS servers  # noqa: E501

        :return: The dns_servers of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: list[str]
        """
        return self._dns_servers

    @dns_servers.setter
    def dns_servers(self, dns_servers):
        """Sets the dns_servers of this SystemInitSpecV5Global.

        Array of IP addresses for the DNS servers  # noqa: E501

        :param dns_servers: The dns_servers of this SystemInitSpecV5Global.  # noqa: E501
        :type: list[str]
        """

        self._dns_servers = dns_servers

    @property
    def syslog_servers(self):
        """Gets the syslog_servers of this SystemInitSpecV5Global.  # noqa: E501

        Array of IP addresses for the Syslog servers  # noqa: E501

        :return: The syslog_servers of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: list[str]
        """
        return self._syslog_servers

    @syslog_servers.setter
    def syslog_servers(self, syslog_servers):
        """Sets the syslog_servers of this SystemInitSpecV5Global.

        Array of IP addresses for the Syslog servers  # noqa: E501

        :param syslog_servers: The syslog_servers of this SystemInitSpecV5Global.  # noqa: E501
        :type: list[str]
        """

        self._syslog_servers = syslog_servers

    @property
    def cluster_type(self):
        """Gets the cluster_type of this SystemInitSpecV5Global.  # noqa: E501

        Type of cluster  # noqa: E501

        :return: The cluster_type of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this SystemInitSpecV5Global.

        Type of cluster  # noqa: E501

        :param cluster_type: The cluster_type of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """
        allowed_values = ["STANDARD", "VSAN2NODE", "DYNAMIC_NODE"]  # noqa: E501
        if cluster_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cluster_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cluster_type, allowed_values)
            )

        self._cluster_type = cluster_type

    @property
    def cluster_vsan_prefix_length_ipv6(self):
        """Gets the cluster_vsan_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The cluster_vsan_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: int
        """
        return self._cluster_vsan_prefix_length_ipv6

    @cluster_vsan_prefix_length_ipv6.setter
    def cluster_vsan_prefix_length_ipv6(self, cluster_vsan_prefix_length_ipv6):
        """Sets the cluster_vsan_prefix_length_ipv6 of this SystemInitSpecV5Global.

        Internal use only  # noqa: E501

        :param cluster_vsan_prefix_length_ipv6: The cluster_vsan_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :type: int
        """

        self._cluster_vsan_prefix_length_ipv6 = cluster_vsan_prefix_length_ipv6

    @property
    def cluster_vmotion_prefix_length_ipv6(self):
        """Gets the cluster_vmotion_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The cluster_vmotion_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: int
        """
        return self._cluster_vmotion_prefix_length_ipv6

    @cluster_vmotion_prefix_length_ipv6.setter
    def cluster_vmotion_prefix_length_ipv6(self, cluster_vmotion_prefix_length_ipv6):
        """Sets the cluster_vmotion_prefix_length_ipv6 of this SystemInitSpecV5Global.

        Internal use only  # noqa: E501

        :param cluster_vmotion_prefix_length_ipv6: The cluster_vmotion_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :type: int
        """

        self._cluster_vmotion_prefix_length_ipv6 = cluster_vmotion_prefix_length_ipv6

    @property
    def cluster_management_prefix_length_ipv6(self):
        """Gets the cluster_management_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The cluster_management_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: int
        """
        return self._cluster_management_prefix_length_ipv6

    @cluster_management_prefix_length_ipv6.setter
    def cluster_management_prefix_length_ipv6(self, cluster_management_prefix_length_ipv6):
        """Sets the cluster_management_prefix_length_ipv6 of this SystemInitSpecV5Global.

        Internal use only  # noqa: E501

        :param cluster_management_prefix_length_ipv6: The cluster_management_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :type: int
        """

        self._cluster_management_prefix_length_ipv6 = cluster_management_prefix_length_ipv6

    @property
    def cluster_management_gateway_ipv6(self):
        """Gets the cluster_management_gateway_ipv6 of this SystemInitSpecV5Global.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The cluster_management_gateway_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_management_gateway_ipv6

    @cluster_management_gateway_ipv6.setter
    def cluster_management_gateway_ipv6(self, cluster_management_gateway_ipv6):
        """Sets the cluster_management_gateway_ipv6 of this SystemInitSpecV5Global.

        Internal use only  # noqa: E501

        :param cluster_management_gateway_ipv6: The cluster_management_gateway_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_management_gateway_ipv6 = cluster_management_gateway_ipv6

    @property
    def cluster_systemvm_netmask(self):
        """Gets the cluster_systemvm_netmask of this SystemInitSpecV5Global.  # noqa: E501

        Subnet mask for cluster management nodes  # noqa: E501

        :return: The cluster_systemvm_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_systemvm_netmask

    @cluster_systemvm_netmask.setter
    def cluster_systemvm_netmask(self, cluster_systemvm_netmask):
        """Sets the cluster_systemvm_netmask of this SystemInitSpecV5Global.

        Subnet mask for cluster management nodes  # noqa: E501

        :param cluster_systemvm_netmask: The cluster_systemvm_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_systemvm_netmask = cluster_systemvm_netmask

    @property
    def cluster_systemvm_gateway(self):
        """Gets the cluster_systemvm_gateway of this SystemInitSpecV5Global.  # noqa: E501

        Gateway address for cluster management nodes  # noqa: E501

        :return: The cluster_systemvm_gateway of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_systemvm_gateway

    @cluster_systemvm_gateway.setter
    def cluster_systemvm_gateway(self, cluster_systemvm_gateway):
        """Sets the cluster_systemvm_gateway of this SystemInitSpecV5Global.

        Gateway address for cluster management nodes  # noqa: E501

        :param cluster_systemvm_gateway: The cluster_systemvm_gateway of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_systemvm_gateway = cluster_systemvm_gateway

    @property
    def cluster_systemvm_prefix_length_ipv6(self):
        """Gets the cluster_systemvm_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The cluster_systemvm_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: int
        """
        return self._cluster_systemvm_prefix_length_ipv6

    @cluster_systemvm_prefix_length_ipv6.setter
    def cluster_systemvm_prefix_length_ipv6(self, cluster_systemvm_prefix_length_ipv6):
        """Sets the cluster_systemvm_prefix_length_ipv6 of this SystemInitSpecV5Global.

        Internal use only  # noqa: E501

        :param cluster_systemvm_prefix_length_ipv6: The cluster_systemvm_prefix_length_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :type: int
        """

        self._cluster_systemvm_prefix_length_ipv6 = cluster_systemvm_prefix_length_ipv6

    @property
    def cluster_systemvm_gateway_ipv6(self):
        """Gets the cluster_systemvm_gateway_ipv6 of this SystemInitSpecV5Global.  # noqa: E501

        Internal use only  # noqa: E501

        :return: The cluster_systemvm_gateway_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_systemvm_gateway_ipv6

    @cluster_systemvm_gateway_ipv6.setter
    def cluster_systemvm_gateway_ipv6(self, cluster_systemvm_gateway_ipv6):
        """Sets the cluster_systemvm_gateway_ipv6 of this SystemInitSpecV5Global.

        Internal use only  # noqa: E501

        :param cluster_systemvm_gateway_ipv6: The cluster_systemvm_gateway_ipv6 of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_systemvm_gateway_ipv6 = cluster_systemvm_gateway_ipv6

    @property
    def cluster_management_netmask(self):
        """Gets the cluster_management_netmask of this SystemInitSpecV5Global.  # noqa: E501

        Subnet mask for cluster management nodes  # noqa: E501

        :return: The cluster_management_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_management_netmask

    @cluster_management_netmask.setter
    def cluster_management_netmask(self, cluster_management_netmask):
        """Sets the cluster_management_netmask of this SystemInitSpecV5Global.

        Subnet mask for cluster management nodes  # noqa: E501

        :param cluster_management_netmask: The cluster_management_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_management_netmask = cluster_management_netmask

    @property
    def cluster_management_gateway(self):
        """Gets the cluster_management_gateway of this SystemInitSpecV5Global.  # noqa: E501

        Gateway address for cluster management nodes  # noqa: E501

        :return: The cluster_management_gateway of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_management_gateway

    @cluster_management_gateway.setter
    def cluster_management_gateway(self, cluster_management_gateway):
        """Sets the cluster_management_gateway of this SystemInitSpecV5Global.

        Gateway address for cluster management nodes  # noqa: E501

        :param cluster_management_gateway: The cluster_management_gateway of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_management_gateway = cluster_management_gateway

    @property
    def cluster_vsan_netmask(self):
        """Gets the cluster_vsan_netmask of this SystemInitSpecV5Global.  # noqa: E501

        Subnet mask for the vSAN cluster  # noqa: E501

        :return: The cluster_vsan_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_vsan_netmask

    @cluster_vsan_netmask.setter
    def cluster_vsan_netmask(self, cluster_vsan_netmask):
        """Sets the cluster_vsan_netmask of this SystemInitSpecV5Global.

        Subnet mask for the vSAN cluster  # noqa: E501

        :param cluster_vsan_netmask: The cluster_vsan_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_vsan_netmask = cluster_vsan_netmask

    @property
    def cluster_vmotion_netmask(self):
        """Gets the cluster_vmotion_netmask of this SystemInitSpecV5Global.  # noqa: E501

        Subnet mask for the vSphere vMotion cluster  # noqa: E501

        :return: The cluster_vmotion_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_vmotion_netmask

    @cluster_vmotion_netmask.setter
    def cluster_vmotion_netmask(self, cluster_vmotion_netmask):
        """Sets the cluster_vmotion_netmask of this SystemInitSpecV5Global.

        Subnet mask for the vSphere vMotion cluster  # noqa: E501

        :param cluster_vmotion_netmask: The cluster_vmotion_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_vmotion_netmask = cluster_vmotion_netmask

    @property
    def cluster_witness_netmask(self):
        """Gets the cluster_witness_netmask of this SystemInitSpecV5Global.  # noqa: E501

        Subnet mask for the witness nodes  # noqa: E501

        :return: The cluster_witness_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_witness_netmask

    @cluster_witness_netmask.setter
    def cluster_witness_netmask(self, cluster_witness_netmask):
        """Sets the cluster_witness_netmask of this SystemInitSpecV5Global.

        Subnet mask for the witness nodes  # noqa: E501

        :param cluster_witness_netmask: The cluster_witness_netmask of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_witness_netmask = cluster_witness_netmask

    @property
    def cluster_witness_gateway(self):
        """Gets the cluster_witness_gateway of this SystemInitSpecV5Global.  # noqa: E501

        Gateway address for the witness nodes  # noqa: E501

        :return: The cluster_witness_gateway of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._cluster_witness_gateway

    @cluster_witness_gateway.setter
    def cluster_witness_gateway(self, cluster_witness_gateway):
        """Sets the cluster_witness_gateway of this SystemInitSpecV5Global.

        Gateway address for the witness nodes  # noqa: E501

        :param cluster_witness_gateway: The cluster_witness_gateway of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._cluster_witness_gateway = cluster_witness_gateway

    @property
    def top_level_domain(self):
        """Gets the top_level_domain of this SystemInitSpecV5Global.  # noqa: E501

        Top-level domain name  # noqa: E501

        :return: The top_level_domain of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: str
        """
        return self._top_level_domain

    @top_level_domain.setter
    def top_level_domain(self, top_level_domain):
        """Sets the top_level_domain of this SystemInitSpecV5Global.

        Top-level domain name  # noqa: E501

        :param top_level_domain: The top_level_domain of this SystemInitSpecV5Global.  # noqa: E501
        :type: str
        """

        self._top_level_domain = top_level_domain

    @property
    def ha_isolation_addresses(self):
        """Gets the ha_isolation_addresses of this SystemInitSpecV5Global.  # noqa: E501

        An array of the IP addresses for the vSphere HA isolation  # noqa: E501

        :return: The ha_isolation_addresses of this SystemInitSpecV5Global.  # noqa: E501
        :rtype: list[str]
        """
        return self._ha_isolation_addresses

    @ha_isolation_addresses.setter
    def ha_isolation_addresses(self, ha_isolation_addresses):
        """Sets the ha_isolation_addresses of this SystemInitSpecV5Global.

        An array of the IP addresses for the vSphere HA isolation  # noqa: E501

        :param ha_isolation_addresses: The ha_isolation_addresses of this SystemInitSpecV5Global.  # noqa: E501
        :type: list[str]
        """

        self._ha_isolation_addresses = ha_isolation_addresses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SystemInitSpecV5Global, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SystemInitSpecV5Global):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
