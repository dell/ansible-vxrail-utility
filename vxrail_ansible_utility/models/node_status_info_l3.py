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

class NodeStatusInfoL3(object):
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
        'id': 'str',
        'model': 'str',
        'serial_number': 'str',
        'system_version': 'NodeVersionInfo',
        'appliance_id': 'str',
        'compatible_status': 'str',
        'compatible_messages': 'list[str]',
        'incompatible_components': 'list[IncompatibleComponentsInfo]'
    }

    attribute_map = {
        'id': 'id',
        'model': 'model',
        'serial_number': 'serial_number',
        'system_version': 'system_version',
        'appliance_id': 'appliance_id',
        'compatible_status': 'compatible_status',
        'compatible_messages': 'compatible_messages',
        'incompatible_components': 'incompatible_components'
    }

    def __init__(self, id=None, model=None, serial_number=None, system_version=None, appliance_id=None, compatible_status=None, compatible_messages=None, incompatible_components=None):  # noqa: E501
        """NodeStatusInfoL3 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._model = None
        self._serial_number = None
        self._system_version = None
        self._appliance_id = None
        self._compatible_status = None
        self._compatible_messages = None
        self._incompatible_components = None
        self.discriminator = None
        self.id = id
        self.model = model
        self.serial_number = serial_number
        self.system_version = system_version
        self.appliance_id = appliance_id
        self.compatible_status = compatible_status
        self.compatible_messages = compatible_messages
        self.incompatible_components = incompatible_components

    @property
    def id(self):
        """Gets the id of this NodeStatusInfoL3.  # noqa: E501

        id of node  # noqa: E501

        :return: The id of this NodeStatusInfoL3.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStatusInfoL3.

        id of node  # noqa: E501

        :param id: The id of this NodeStatusInfoL3.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def model(self):
        """Gets the model of this NodeStatusInfoL3.  # noqa: E501

        mode of node  # noqa: E501

        :return: The model of this NodeStatusInfoL3.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this NodeStatusInfoL3.

        mode of node  # noqa: E501

        :param model: The model of this NodeStatusInfoL3.  # noqa: E501
        :type: str
        """
        if model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def serial_number(self):
        """Gets the serial_number of this NodeStatusInfoL3.  # noqa: E501

        Serial number of node  # noqa: E501

        :return: The serial_number of this NodeStatusInfoL3.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this NodeStatusInfoL3.

        Serial number of node  # noqa: E501

        :param serial_number: The serial_number of this NodeStatusInfoL3.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def system_version(self):
        """Gets the system_version of this NodeStatusInfoL3.  # noqa: E501


        :return: The system_version of this NodeStatusInfoL3.  # noqa: E501
        :rtype: NodeVersionInfo
        """
        return self._system_version

    @system_version.setter
    def system_version(self, system_version):
        """Sets the system_version of this NodeStatusInfoL3.


        :param system_version: The system_version of this NodeStatusInfoL3.  # noqa: E501
        :type: NodeVersionInfo
        """
        if system_version is None:
            raise ValueError("Invalid value for `system_version`, must not be `None`")  # noqa: E501

        self._system_version = system_version

    @property
    def appliance_id(self):
        """Gets the appliance_id of this NodeStatusInfoL3.  # noqa: E501

        Appliance ID of node  # noqa: E501

        :return: The appliance_id of this NodeStatusInfoL3.  # noqa: E501
        :rtype: str
        """
        return self._appliance_id

    @appliance_id.setter
    def appliance_id(self, appliance_id):
        """Sets the appliance_id of this NodeStatusInfoL3.

        Appliance ID of node  # noqa: E501

        :param appliance_id: The appliance_id of this NodeStatusInfoL3.  # noqa: E501
        :type: str
        """
        if appliance_id is None:
            raise ValueError("Invalid value for `appliance_id`, must not be `None`")  # noqa: E501

        self._appliance_id = appliance_id

    @property
    def compatible_status(self):
        """Gets the compatible_status of this NodeStatusInfoL3.  # noqa: E501

        Node compatibility result after pre-check  # noqa: E501

        :return: The compatible_status of this NodeStatusInfoL3.  # noqa: E501
        :rtype: str
        """
        return self._compatible_status

    @compatible_status.setter
    def compatible_status(self, compatible_status):
        """Sets the compatible_status of this NodeStatusInfoL3.

        Node compatibility result after pre-check  # noqa: E501

        :param compatible_status: The compatible_status of this NodeStatusInfoL3.  # noqa: E501
        :type: str
        """
        if compatible_status is None:
            raise ValueError("Invalid value for `compatible_status`, must not be `None`")  # noqa: E501

        self._compatible_status = compatible_status

    @property
    def compatible_messages(self):
        """Gets the compatible_messages of this NodeStatusInfoL3.  # noqa: E501

        Incompatible details  # noqa: E501

        :return: The compatible_messages of this NodeStatusInfoL3.  # noqa: E501
        :rtype: list[str]
        """
        return self._compatible_messages

    @compatible_messages.setter
    def compatible_messages(self, compatible_messages):
        """Sets the compatible_messages of this NodeStatusInfoL3.

        Incompatible details  # noqa: E501

        :param compatible_messages: The compatible_messages of this NodeStatusInfoL3.  # noqa: E501
        :type: list[str]
        """
        if compatible_messages is None:
            raise ValueError("Invalid value for `compatible_messages`, must not be `None`")  # noqa: E501

        self._compatible_messages = compatible_messages

    @property
    def incompatible_components(self):
        """Gets the incompatible_components of this NodeStatusInfoL3.  # noqa: E501

        Incompatible components  # noqa: E501

        :return: The incompatible_components of this NodeStatusInfoL3.  # noqa: E501
        :rtype: list[IncompatibleComponentsInfo]
        """
        return self._incompatible_components

    @incompatible_components.setter
    def incompatible_components(self, incompatible_components):
        """Sets the incompatible_components of this NodeStatusInfoL3.

        Incompatible components  # noqa: E501

        :param incompatible_components: The incompatible_components of this NodeStatusInfoL3.  # noqa: E501
        :type: list[IncompatibleComponentsInfo]
        """
        if incompatible_components is None:
            raise ValueError("Invalid value for `incompatible_components`, must not be `None`")  # noqa: E501

        self._incompatible_components = incompatible_components

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
        if issubclass(NodeStatusInfoL3, dict):
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
        if not isinstance(other, NodeStatusInfoL3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
