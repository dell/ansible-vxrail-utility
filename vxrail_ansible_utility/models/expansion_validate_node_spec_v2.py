# coding: utf-8

"""
    VxRail Cluster and System Management

    APIs for cluster management and system management  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExpansionValidateNodeSpecV2(object):
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
        'sn': 'str',
        'customer_supplied': 'CustomerSuppliedSpec',
        'hostname': 'str',
        'management_account': 'Account',
        'root_password': 'str',
        'networks': 'HostNetworkConfiguration',
        'geo_location': 'GeoLocation'
    }

    attribute_map = {
        'sn': 'sn',
        'customer_supplied': 'customer_supplied',
        'hostname': 'hostname',
        'management_account': 'management_account',
        'root_password': 'root_password',
        'networks': 'networks',
        'geo_location': 'geo_location'
    }

    def __init__(self, sn=None, customer_supplied=None, hostname=None, management_account=None, root_password=None, networks=None, geo_location=None):  # noqa: E501
        """ExpansionValidateNodeSpecV2 - a model defined in Swagger"""  # noqa: E501
        self._sn = None
        self._customer_supplied = None
        self._hostname = None
        self._management_account = None
        self._root_password = None
        self._networks = None
        self._geo_location = None
        self.discriminator = None
        if sn is not None:
            self.sn = sn
        if customer_supplied is not None:
            self.customer_supplied = customer_supplied
        self.hostname = hostname
        self.management_account = management_account
        self.root_password = root_password
        self.networks = networks
        if geo_location is not None:
            self.geo_location = geo_location

    @property
    def sn(self):
        """Gets the sn of this ExpansionValidateNodeSpecV2.  # noqa: E501


        :return: The sn of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this ExpansionValidateNodeSpecV2.


        :param sn: The sn of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :type: str
        """

        self._sn = sn

    @property
    def customer_supplied(self):
        """Gets the customer_supplied of this ExpansionValidateNodeSpecV2.  # noqa: E501


        :return: The customer_supplied of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :rtype: CustomerSuppliedSpec
        """
        return self._customer_supplied

    @customer_supplied.setter
    def customer_supplied(self, customer_supplied):
        """Sets the customer_supplied of this ExpansionValidateNodeSpecV2.


        :param customer_supplied: The customer_supplied of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :type: CustomerSuppliedSpec
        """

        self._customer_supplied = customer_supplied

    @property
    def hostname(self):
        """Gets the hostname of this ExpansionValidateNodeSpecV2.  # noqa: E501


        :return: The hostname of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ExpansionValidateNodeSpecV2.


        :param hostname: The hostname of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :type: str
        """
        if hostname is None:
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def management_account(self):
        """Gets the management_account of this ExpansionValidateNodeSpecV2.  # noqa: E501


        :return: The management_account of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :rtype: Account
        """
        return self._management_account

    @management_account.setter
    def management_account(self, management_account):
        """Sets the management_account of this ExpansionValidateNodeSpecV2.


        :param management_account: The management_account of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :type: Account
        """
        if management_account is None:
            raise ValueError("Invalid value for `management_account`, must not be `None`")  # noqa: E501

        self._management_account = management_account

    @property
    def root_password(self):
        """Gets the root_password of this ExpansionValidateNodeSpecV2.  # noqa: E501

        Root password of host.  # noqa: E501

        :return: The root_password of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :rtype: str
        """
        return self._root_password

    @root_password.setter
    def root_password(self, root_password):
        """Sets the root_password of this ExpansionValidateNodeSpecV2.

        Root password of host.  # noqa: E501

        :param root_password: The root_password of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :type: str
        """
        if root_password is None:
            raise ValueError("Invalid value for `root_password`, must not be `None`")  # noqa: E501

        self._root_password = root_password

    @property
    def networks(self):
        """Gets the networks of this ExpansionValidateNodeSpecV2.  # noqa: E501


        :return: The networks of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :rtype: HostNetworkConfiguration
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this ExpansionValidateNodeSpecV2.


        :param networks: The networks of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :type: HostNetworkConfiguration
        """
        if networks is None:
            raise ValueError("Invalid value for `networks`, must not be `None`")  # noqa: E501

        self._networks = networks

    @property
    def geo_location(self):
        """Gets the geo_location of this ExpansionValidateNodeSpecV2.  # noqa: E501


        :return: The geo_location of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :rtype: GeoLocation
        """
        return self._geo_location

    @geo_location.setter
    def geo_location(self, geo_location):
        """Sets the geo_location of this ExpansionValidateNodeSpecV2.


        :param geo_location: The geo_location of this ExpansionValidateNodeSpecV2.  # noqa: E501
        :type: GeoLocation
        """

        self._geo_location = geo_location

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
        if issubclass(ExpansionValidateNodeSpecV2, dict):
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
        if not isinstance(other, ExpansionValidateNodeSpecV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
