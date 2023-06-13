# coding: utf-8

"""
    Day1 Bring Up Configuration

    The set of Day 1 Bring Up Configuration API(s) are used to deploy VxRail cluster.  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SystemInitSpecV3Vcenter(object):
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
        'customer_supplied': 'bool',
        'customer_supplied_vc_name_or_ip': 'str',
        'vxrail_supplied_vc_ip': 'str',
        'vxrail_supplied_vc_name': 'str',
        'datacenter_name': 'str',
        'cluster_name': 'str',
        'accounts': 'SystemInitSpecV3VcenterAccounts',
        'sso_domain': 'SystemInitSpecV3VcenterSsoDomain'
    }

    attribute_map = {
        'customer_supplied': 'customer_supplied',
        'customer_supplied_vc_name_or_ip': 'customer_supplied_vc_name_or_ip',
        'vxrail_supplied_vc_ip': 'vxrail_supplied_vc_ip',
        'vxrail_supplied_vc_name': 'vxrail_supplied_vc_name',
        'datacenter_name': 'datacenter_name',
        'cluster_name': 'cluster_name',
        'accounts': 'accounts',
        'sso_domain': 'sso_domain'
    }

    def __init__(self, customer_supplied=None, customer_supplied_vc_name_or_ip=None, vxrail_supplied_vc_ip=None, vxrail_supplied_vc_name=None, datacenter_name=None, cluster_name=None, accounts=None, sso_domain=None):  # noqa: E501
        """SystemInitSpecV3Vcenter - a model defined in Swagger"""  # noqa: E501
        self._customer_supplied = None
        self._customer_supplied_vc_name_or_ip = None
        self._vxrail_supplied_vc_ip = None
        self._vxrail_supplied_vc_name = None
        self._datacenter_name = None
        self._cluster_name = None
        self._accounts = None
        self._sso_domain = None
        self.discriminator = None
        if customer_supplied is not None:
            self.customer_supplied = customer_supplied
        if customer_supplied_vc_name_or_ip is not None:
            self.customer_supplied_vc_name_or_ip = customer_supplied_vc_name_or_ip
        if vxrail_supplied_vc_ip is not None:
            self.vxrail_supplied_vc_ip = vxrail_supplied_vc_ip
        if vxrail_supplied_vc_name is not None:
            self.vxrail_supplied_vc_name = vxrail_supplied_vc_name
        if datacenter_name is not None:
            self.datacenter_name = datacenter_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if accounts is not None:
            self.accounts = accounts
        if sso_domain is not None:
            self.sso_domain = sso_domain

    @property
    def customer_supplied(self):
        """Gets the customer_supplied of this SystemInitSpecV3Vcenter.  # noqa: E501

        Whether the vCenter server is customer supplied (external) or VxRail integrated (internal). Supported values are true for customer supplied and false for integrated.  # noqa: E501

        :return: The customer_supplied of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: bool
        """
        return self._customer_supplied

    @customer_supplied.setter
    def customer_supplied(self, customer_supplied):
        """Sets the customer_supplied of this SystemInitSpecV3Vcenter.

        Whether the vCenter server is customer supplied (external) or VxRail integrated (internal). Supported values are true for customer supplied and false for integrated.  # noqa: E501

        :param customer_supplied: The customer_supplied of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: bool
        """

        self._customer_supplied = customer_supplied

    @property
    def customer_supplied_vc_name_or_ip(self):
        """Gets the customer_supplied_vc_name_or_ip of this SystemInitSpecV3Vcenter.  # noqa: E501

        The IP address or FQDN of the vCenter server. This property is only provided if the vCenter server is customer supplied.  # noqa: E501

        :return: The customer_supplied_vc_name_or_ip of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: str
        """
        return self._customer_supplied_vc_name_or_ip

    @customer_supplied_vc_name_or_ip.setter
    def customer_supplied_vc_name_or_ip(self, customer_supplied_vc_name_or_ip):
        """Sets the customer_supplied_vc_name_or_ip of this SystemInitSpecV3Vcenter.

        The IP address or FQDN of the vCenter server. This property is only provided if the vCenter server is customer supplied.  # noqa: E501

        :param customer_supplied_vc_name_or_ip: The customer_supplied_vc_name_or_ip of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: str
        """

        self._customer_supplied_vc_name_or_ip = customer_supplied_vc_name_or_ip

    @property
    def vxrail_supplied_vc_ip(self):
        """Gets the vxrail_supplied_vc_ip of this SystemInitSpecV3Vcenter.  # noqa: E501

        The IP address of the VxRail integrated vCenter server. This property is only provided if the vCenter server is VxRail integrated.  # noqa: E501

        :return: The vxrail_supplied_vc_ip of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: str
        """
        return self._vxrail_supplied_vc_ip

    @vxrail_supplied_vc_ip.setter
    def vxrail_supplied_vc_ip(self, vxrail_supplied_vc_ip):
        """Sets the vxrail_supplied_vc_ip of this SystemInitSpecV3Vcenter.

        The IP address of the VxRail integrated vCenter server. This property is only provided if the vCenter server is VxRail integrated.  # noqa: E501

        :param vxrail_supplied_vc_ip: The vxrail_supplied_vc_ip of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: str
        """

        self._vxrail_supplied_vc_ip = vxrail_supplied_vc_ip

    @property
    def vxrail_supplied_vc_name(self):
        """Gets the vxrail_supplied_vc_name of this SystemInitSpecV3Vcenter.  # noqa: E501

        The hostname of the VxRail integrated vCenter server. This property is only provided if the vCenter server is VxRail integrated.  # noqa: E501

        :return: The vxrail_supplied_vc_name of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: str
        """
        return self._vxrail_supplied_vc_name

    @vxrail_supplied_vc_name.setter
    def vxrail_supplied_vc_name(self, vxrail_supplied_vc_name):
        """Sets the vxrail_supplied_vc_name of this SystemInitSpecV3Vcenter.

        The hostname of the VxRail integrated vCenter server. This property is only provided if the vCenter server is VxRail integrated.  # noqa: E501

        :param vxrail_supplied_vc_name: The vxrail_supplied_vc_name of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: str
        """

        self._vxrail_supplied_vc_name = vxrail_supplied_vc_name

    @property
    def datacenter_name(self):
        """Gets the datacenter_name of this SystemInitSpecV3Vcenter.  # noqa: E501

        The name of the datacenter. This property is only provided if the vCenter server is customer supplied.  # noqa: E501

        :return: The datacenter_name of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: str
        """
        return self._datacenter_name

    @datacenter_name.setter
    def datacenter_name(self, datacenter_name):
        """Sets the datacenter_name of this SystemInitSpecV3Vcenter.

        The name of the datacenter. This property is only provided if the vCenter server is customer supplied.  # noqa: E501

        :param datacenter_name: The datacenter_name of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: str
        """

        self._datacenter_name = datacenter_name

    @property
    def cluster_name(self):
        """Gets the cluster_name of this SystemInitSpecV3Vcenter.  # noqa: E501

        The name of the cluster. This property is only provided if the vCenter server is customer supplied.  # noqa: E501

        :return: The cluster_name of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this SystemInitSpecV3Vcenter.

        The name of the cluster. This property is only provided if the vCenter server is customer supplied.  # noqa: E501

        :param cluster_name: The cluster_name of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def accounts(self):
        """Gets the accounts of this SystemInitSpecV3Vcenter.  # noqa: E501


        :return: The accounts of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: SystemInitSpecV3VcenterAccounts
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this SystemInitSpecV3Vcenter.


        :param accounts: The accounts of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: SystemInitSpecV3VcenterAccounts
        """

        self._accounts = accounts

    @property
    def sso_domain(self):
        """Gets the sso_domain of this SystemInitSpecV3Vcenter.  # noqa: E501


        :return: The sso_domain of this SystemInitSpecV3Vcenter.  # noqa: E501
        :rtype: SystemInitSpecV3VcenterSsoDomain
        """
        return self._sso_domain

    @sso_domain.setter
    def sso_domain(self, sso_domain):
        """Sets the sso_domain of this SystemInitSpecV3Vcenter.


        :param sso_domain: The sso_domain of this SystemInitSpecV3Vcenter.  # noqa: E501
        :type: SystemInitSpecV3VcenterSsoDomain
        """

        self._sso_domain = sso_domain

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
        if issubclass(SystemInitSpecV3Vcenter, dict):
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
        if not isinstance(other, SystemInitSpecV3Vcenter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
