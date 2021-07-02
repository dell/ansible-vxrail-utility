# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 7.0.240
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PrivateExpansionNodeSpec(object):
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
        'customer_supplied': 'CustomerSuppliedSpec',
        'sn': 'str',
        'hostname': 'str',
        'accounts': 'NodeAccount',
        'network': 'list[HostIp]',
        'maintenance_mode': 'bool',
        'geo_location': 'GeoLocation',
        'nic_mappings': 'list[NicUplinkV2]',
        'storage': 'StroageInfoPrivate'
    }

    attribute_map = {
        'customer_supplied': 'customer_supplied',
        'sn': 'sn',
        'hostname': 'hostname',
        'accounts': 'accounts',
        'network': 'network',
        'maintenance_mode': 'maintenance_mode',
        'geo_location': 'geo_location',
        'nic_mappings': 'nic_mappings',
        'storage': 'storage'
    }

    def __init__(self, customer_supplied=None, sn=None, hostname=None, accounts=None, network=None, maintenance_mode=None, geo_location=None, nic_mappings=None, storage=None):  # noqa: E501
        """PrivateExpansionNodeSpec - a model defined in Swagger"""  # noqa: E501
        self._customer_supplied = None
        self._sn = None
        self._hostname = None
        self._accounts = None
        self._network = None
        self._maintenance_mode = None
        self._geo_location = None
        self._nic_mappings = None
        self._storage = None
        self.discriminator = None
        if customer_supplied is not None:
            self.customer_supplied = customer_supplied
        if sn is not None:
            self.sn = sn
        self.hostname = hostname
        self.accounts = accounts
        self.network = network
        if maintenance_mode is not None:
            self.maintenance_mode = maintenance_mode
        if geo_location is not None:
            self.geo_location = geo_location
        self.nic_mappings = nic_mappings
        if storage is not None:
            self.storage = storage

    @property
    def customer_supplied(self):
        """Gets the customer_supplied of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The customer_supplied of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: CustomerSuppliedSpec
        """
        return self._customer_supplied

    @customer_supplied.setter
    def customer_supplied(self, customer_supplied):
        """Sets the customer_supplied of this PrivateExpansionNodeSpec.


        :param customer_supplied: The customer_supplied of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: CustomerSuppliedSpec
        """

        self._customer_supplied = customer_supplied

    @property
    def sn(self):
        """Gets the sn of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The sn of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this PrivateExpansionNodeSpec.


        :param sn: The sn of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def hostname(self):
        """Gets the hostname of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The hostname of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PrivateExpansionNodeSpec.


        :param hostname: The hostname of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def accounts(self):
        """Gets the accounts of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The accounts of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: NodeAccount
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this PrivateExpansionNodeSpec.


        :param accounts: The accounts of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: NodeAccount
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def network(self):
        """Gets the network of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The network of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: list[HostIp]
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this PrivateExpansionNodeSpec.


        :param network: The network of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: list[HostIp]
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def maintenance_mode(self):
        """Gets the maintenance_mode of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The maintenance_mode of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: bool
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, maintenance_mode):
        """Sets the maintenance_mode of this PrivateExpansionNodeSpec.


        :param maintenance_mode: The maintenance_mode of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: bool
        """

        self._maintenance_mode = maintenance_mode

    @property
    def geo_location(self):
        """Gets the geo_location of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The geo_location of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: GeoLocation
        """
        return self._geo_location

    @geo_location.setter
    def geo_location(self, geo_location):
        """Sets the geo_location of this PrivateExpansionNodeSpec.


        :param geo_location: The geo_location of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: GeoLocation
        """

        self._geo_location = geo_location

    @property
    def nic_mappings(self):
        """Gets the nic_mappings of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The nic_mappings of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: list[NicUplinkV2]
        """
        return self._nic_mappings

    @nic_mappings.setter
    def nic_mappings(self, nic_mappings):
        """Sets the nic_mappings of this PrivateExpansionNodeSpec.


        :param nic_mappings: The nic_mappings of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: list[NicUplinkV2]
        """
        if nic_mappings is None:
            raise ValueError("Invalid value for `nic_mappings`, must not be `None`")  # noqa: E501

        self._nic_mappings = nic_mappings

    @property
    def storage(self):
        """Gets the storage of this PrivateExpansionNodeSpec.  # noqa: E501


        :return: The storage of this PrivateExpansionNodeSpec.  # noqa: E501
        :rtype: StroageInfoPrivate
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this PrivateExpansionNodeSpec.


        :param storage: The storage of this PrivateExpansionNodeSpec.  # noqa: E501
        :type: StroageInfoPrivate
        """

        self._storage = storage

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
        if issubclass(PrivateExpansionNodeSpec, dict):
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
        if not isinstance(other, PrivateExpansionNodeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other