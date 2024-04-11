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

class DiscoveredNodeNICProfilesInfo(object):
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
        'name': 'str',
        'description': 'str',
        'configuration_type': 'str',
        'vmnics_mapping': 'list[DiscoveredNodeNICProfilesInfoVmnicsMapping]',
        'selectable_load_balance_policy': 'list[str]',
        'teaming_policy': 'DiscoveredNodeNICProfilesInfoTeamingPolicy'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'configuration_type': 'configuration_type',
        'vmnics_mapping': 'vmnics_mapping',
        'selectable_load_balance_policy': 'selectable_load_balance_policy',
        'teaming_policy': 'teaming_policy'
    }

    def __init__(self, name=None, description=None, configuration_type=None, vmnics_mapping=None, selectable_load_balance_policy=None, teaming_policy=None):  # noqa: E501
        """DiscoveredNodeNICProfilesInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._configuration_type = None
        self._vmnics_mapping = None
        self._selectable_load_balance_policy = None
        self._teaming_policy = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if configuration_type is not None:
            self.configuration_type = configuration_type
        if vmnics_mapping is not None:
            self.vmnics_mapping = vmnics_mapping
        if selectable_load_balance_policy is not None:
            self.selectable_load_balance_policy = selectable_load_balance_policy
        if teaming_policy is not None:
            self.teaming_policy = teaming_policy

    @property
    def name(self):
        """Gets the name of this DiscoveredNodeNICProfilesInfo.  # noqa: E501

        Name of the NIC profile  # noqa: E501

        :return: The name of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiscoveredNodeNICProfilesInfo.

        Name of the NIC profile  # noqa: E501

        :param name: The name of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DiscoveredNodeNICProfilesInfo.  # noqa: E501

        Infomation about NIC profile  # noqa: E501

        :return: The description of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DiscoveredNodeNICProfilesInfo.

        Infomation about NIC profile  # noqa: E501

        :param description: The description of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def configuration_type(self):
        """Gets the configuration_type of this DiscoveredNodeNICProfilesInfo.  # noqa: E501

        pre-configured  # noqa: E501

        :return: The configuration_type of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :rtype: str
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """Sets the configuration_type of this DiscoveredNodeNICProfilesInfo.

        pre-configured  # noqa: E501

        :param configuration_type: The configuration_type of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :type: str
        """

        self._configuration_type = configuration_type

    @property
    def vmnics_mapping(self):
        """Gets the vmnics_mapping of this DiscoveredNodeNICProfilesInfo.  # noqa: E501

        The mapping between uplinks and vmnics  # noqa: E501

        :return: The vmnics_mapping of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :rtype: list[DiscoveredNodeNICProfilesInfoVmnicsMapping]
        """
        return self._vmnics_mapping

    @vmnics_mapping.setter
    def vmnics_mapping(self, vmnics_mapping):
        """Sets the vmnics_mapping of this DiscoveredNodeNICProfilesInfo.

        The mapping between uplinks and vmnics  # noqa: E501

        :param vmnics_mapping: The vmnics_mapping of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :type: list[DiscoveredNodeNICProfilesInfoVmnicsMapping]
        """

        self._vmnics_mapping = vmnics_mapping

    @property
    def selectable_load_balance_policy(self):
        """Gets the selectable_load_balance_policy of this DiscoveredNodeNICProfilesInfo.  # noqa: E501

        Load balance policies  # noqa: E501

        :return: The selectable_load_balance_policy of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._selectable_load_balance_policy

    @selectable_load_balance_policy.setter
    def selectable_load_balance_policy(self, selectable_load_balance_policy):
        """Sets the selectable_load_balance_policy of this DiscoveredNodeNICProfilesInfo.

        Load balance policies  # noqa: E501

        :param selectable_load_balance_policy: The selectable_load_balance_policy of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["LOADBALANCE_SRCMAC", "FAILOVER_EXPLICIT", "LOADBALANCE_LOADBASED", "LOADBALANCE_SRCID"]  # noqa: E501
        if not set(selectable_load_balance_policy).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `selectable_load_balance_policy` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(selectable_load_balance_policy) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._selectable_load_balance_policy = selectable_load_balance_policy

    @property
    def teaming_policy(self):
        """Gets the teaming_policy of this DiscoveredNodeNICProfilesInfo.  # noqa: E501


        :return: The teaming_policy of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :rtype: DiscoveredNodeNICProfilesInfoTeamingPolicy
        """
        return self._teaming_policy

    @teaming_policy.setter
    def teaming_policy(self, teaming_policy):
        """Sets the teaming_policy of this DiscoveredNodeNICProfilesInfo.


        :param teaming_policy: The teaming_policy of this DiscoveredNodeNICProfilesInfo.  # noqa: E501
        :type: DiscoveredNodeNICProfilesInfoTeamingPolicy
        """

        self._teaming_policy = teaming_policy

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
        if issubclass(DiscoveredNodeNICProfilesInfo, dict):
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
        if not isinstance(other, DiscoveredNodeNICProfilesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other