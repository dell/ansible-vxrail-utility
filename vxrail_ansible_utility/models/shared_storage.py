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

class SharedStorage(object):
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
        'type': 'str',
        'protocol': 'str',
        'is_primary': 'bool',
        'datastore_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'protocol': 'protocol',
        'is_primary': 'is_primary',
        'datastore_id': 'datastore_id'
    }

    def __init__(self, name=None, type=None, protocol=None, is_primary=None, datastore_id=None):  # noqa: E501
        """SharedStorage - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._protocol = None
        self._is_primary = None
        self._datastore_id = None
        self.discriminator = None
        self.name = name
        self.type = type
        if protocol is not None:
            self.protocol = protocol
        self.is_primary = is_primary
        if datastore_id is not None:
            self.datastore_id = datastore_id

    @property
    def name(self):
        """Gets the name of this SharedStorage.  # noqa: E501

        The shared datastore name  # noqa: E501

        :return: The name of this SharedStorage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SharedStorage.

        The shared datastore name  # noqa: E501

        :param name: The name of this SharedStorage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this SharedStorage.  # noqa: E501

        The shared datastore type  # noqa: E501

        :return: The type of this SharedStorage.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SharedStorage.

        The shared datastore type  # noqa: E501

        :param type: The type of this SharedStorage.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["VSAN", "VMFS", "NFS", "VVOL", "HCI_MESH"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def protocol(self):
        """Gets the protocol of this SharedStorage.  # noqa: E501

        The storage protocol used by the host  # noqa: E501

        :return: The protocol of this SharedStorage.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SharedStorage.

        The storage protocol used by the host  # noqa: E501

        :param protocol: The protocol of this SharedStorage.  # noqa: E501
        :type: str
        """
        allowed_values = ["FC", "SCSI", "NFS", "VSAN", "OTHER", "FC-NVMe", "TCP-NVMe", "ISCSI", "UNKNOWN"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def is_primary(self):
        """Gets the is_primary of this SharedStorage.  # noqa: E501

        Whether the datastore is the primary datastore where VxRail Manager is deployed on it  # noqa: E501

        :return: The is_primary of this SharedStorage.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """Sets the is_primary of this SharedStorage.

        Whether the datastore is the primary datastore where VxRail Manager is deployed on it  # noqa: E501

        :param is_primary: The is_primary of this SharedStorage.  # noqa: E501
        :type: bool
        """
        if is_primary is None:
            raise ValueError("Invalid value for `is_primary`, must not be `None`")  # noqa: E501

        self._is_primary = is_primary

    @property
    def datastore_id(self):
        """Gets the datastore_id of this SharedStorage.  # noqa: E501

        The storage moid used by the host  # noqa: E501

        :return: The datastore_id of this SharedStorage.  # noqa: E501
        :rtype: str
        """
        return self._datastore_id

    @datastore_id.setter
    def datastore_id(self, datastore_id):
        """Sets the datastore_id of this SharedStorage.

        The storage moid used by the host  # noqa: E501

        :param datastore_id: The datastore_id of this SharedStorage.  # noqa: E501
        :type: str
        """

        self._datastore_id = datastore_id

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
        if issubclass(SharedStorage, dict):
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
        if not isinstance(other, SharedStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
