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

class VxmSystemInfo(object):
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
        'description': 'str',
        'version': 'str',
        'installed_time': 'int',
        'health': 'str',
        'network_connected': 'bool',
        'vc_connected': 'bool',
        'upgrade_status': 'str',
        'installed_components': 'list[InstalledComponent]',
        'cluster_type': 'str',
        'number_of_host': 'int',
        'is_external_vc': 'bool',
        'logical_view_status': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'version': 'version',
        'installed_time': 'installed_time',
        'health': 'health',
        'network_connected': 'network_connected',
        'vc_connected': 'vc_connected',
        'upgrade_status': 'upgrade_status',
        'installed_components': 'installed_components',
        'cluster_type': 'cluster_type',
        'number_of_host': 'number_of_host',
        'is_external_vc': 'is_external_vc',
        'logical_view_status': 'logical_view_status'
    }

    def __init__(self, description=None, version=None, installed_time=None, health=None, network_connected=None, vc_connected=None, upgrade_status=None, installed_components=None, cluster_type=None, number_of_host=None, is_external_vc=None, logical_view_status=None):  # noqa: E501
        """VxmSystemInfo - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._version = None
        self._installed_time = None
        self._health = None
        self._network_connected = None
        self._vc_connected = None
        self._upgrade_status = None
        self._installed_components = None
        self._cluster_type = None
        self._number_of_host = None
        self._is_external_vc = None
        self._logical_view_status = None
        self.discriminator = None
        self.description = description
        self.version = version
        if installed_time is not None:
            self.installed_time = installed_time
        self.health = health
        self.network_connected = network_connected
        self.vc_connected = vc_connected
        if upgrade_status is not None:
            self.upgrade_status = upgrade_status
        if installed_components is not None:
            self.installed_components = installed_components
        self.cluster_type = cluster_type
        self.number_of_host = number_of_host
        self.is_external_vc = is_external_vc
        self.logical_view_status = logical_view_status

    @property
    def description(self):
        """Gets the description of this VxmSystemInfo.  # noqa: E501

        Description of the VxRail system  # noqa: E501

        :return: The description of this VxmSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VxmSystemInfo.

        Description of the VxRail system  # noqa: E501

        :param description: The description of this VxmSystemInfo.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def version(self):
        """Gets the version of this VxmSystemInfo.  # noqa: E501

        Software version of the VxRail appliance  # noqa: E501

        :return: The version of this VxmSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VxmSystemInfo.

        Software version of the VxRail appliance  # noqa: E501

        :param version: The version of this VxmSystemInfo.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def installed_time(self):
        """Gets the installed_time of this VxmSystemInfo.  # noqa: E501

        Time that the VxRail appliance software was installed  # noqa: E501

        :return: The installed_time of this VxmSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._installed_time

    @installed_time.setter
    def installed_time(self, installed_time):
        """Sets the installed_time of this VxmSystemInfo.

        Time that the VxRail appliance software was installed  # noqa: E501

        :param installed_time: The installed_time of this VxmSystemInfo.  # noqa: E501
        :type: int
        """

        self._installed_time = installed_time

    @property
    def health(self):
        """Gets the health of this VxmSystemInfo.  # noqa: E501

        Health status of the VxRail system  # noqa: E501

        :return: The health of this VxmSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this VxmSystemInfo.

        Health status of the VxRail system  # noqa: E501

        :param health: The health of this VxmSystemInfo.  # noqa: E501
        :type: str
        """
        if health is None:
            raise ValueError("Invalid value for `health`, must not be `None`")  # noqa: E501

        self._health = health

    @property
    def network_connected(self):
        """Gets the network_connected of this VxmSystemInfo.  # noqa: E501

        Whether the host is connected to the internet  # noqa: E501

        :return: The network_connected of this VxmSystemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._network_connected

    @network_connected.setter
    def network_connected(self, network_connected):
        """Sets the network_connected of this VxmSystemInfo.

        Whether the host is connected to the internet  # noqa: E501

        :param network_connected: The network_connected of this VxmSystemInfo.  # noqa: E501
        :type: bool
        """
        if network_connected is None:
            raise ValueError("Invalid value for `network_connected`, must not be `None`")  # noqa: E501

        self._network_connected = network_connected

    @property
    def vc_connected(self):
        """Gets the vc_connected of this VxmSystemInfo.  # noqa: E501

        Whether the vCenter is connected  # noqa: E501

        :return: The vc_connected of this VxmSystemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._vc_connected

    @vc_connected.setter
    def vc_connected(self, vc_connected):
        """Sets the vc_connected of this VxmSystemInfo.

        Whether the vCenter is connected  # noqa: E501

        :param vc_connected: The vc_connected of this VxmSystemInfo.  # noqa: E501
        :type: bool
        """
        if vc_connected is None:
            raise ValueError("Invalid value for `vc_connected`, must not be `None`")  # noqa: E501

        self._vc_connected = vc_connected

    @property
    def upgrade_status(self):
        """Gets the upgrade_status of this VxmSystemInfo.  # noqa: E501

        The upgrade status of the VxRail appliance software  # noqa: E501

        :return: The upgrade_status of this VxmSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """Sets the upgrade_status of this VxmSystemInfo.

        The upgrade status of the VxRail appliance software  # noqa: E501

        :param upgrade_status: The upgrade_status of this VxmSystemInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["CANCELLED", "DOWNLOADED", "DOWNLOADING", "ERR_DOWNLOAD", "ERR_PROFILE_PRECHECKER", "ERR_UPGRADED", "ERR_UPGRADE_PRECHECKER", "ERR_UPLOAD", "HAS_NEWER", "LATEST", "PROFILE_PRECHECKED", "UPGRADED", "UPGRADE_PRECHECKING", "UPGRADING", "UPLOADED", "UPLOADING"]  # noqa: E501
        if upgrade_status not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade_status` ({0}), must be one of {1}"  # noqa: E501
                .format(upgrade_status, allowed_values)
            )

        self._upgrade_status = upgrade_status

    @property
    def installed_components(self):
        """Gets the installed_components of this VxmSystemInfo.  # noqa: E501

        Software components installed in the VxRail system  # noqa: E501

        :return: The installed_components of this VxmSystemInfo.  # noqa: E501
        :rtype: list[InstalledComponent]
        """
        return self._installed_components

    @installed_components.setter
    def installed_components(self, installed_components):
        """Sets the installed_components of this VxmSystemInfo.

        Software components installed in the VxRail system  # noqa: E501

        :param installed_components: The installed_components of this VxmSystemInfo.  # noqa: E501
        :type: list[InstalledComponent]
        """

        self._installed_components = installed_components

    @property
    def cluster_type(self):
        """Gets the cluster_type of this VxmSystemInfo.  # noqa: E501

        Cluster configuration of the VxRail system  # noqa: E501

        :return: The cluster_type of this VxmSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this VxmSystemInfo.

        Cluster configuration of the VxRail system  # noqa: E501

        :param cluster_type: The cluster_type of this VxmSystemInfo.  # noqa: E501
        :type: str
        """
        if cluster_type is None:
            raise ValueError("Invalid value for `cluster_type`, must not be `None`")  # noqa: E501

        self._cluster_type = cluster_type

    @property
    def number_of_host(self):
        """Gets the number_of_host of this VxmSystemInfo.  # noqa: E501

        Number of hosts in the cluster  # noqa: E501

        :return: The number_of_host of this VxmSystemInfo.  # noqa: E501
        :rtype: int
        """
        return self._number_of_host

    @number_of_host.setter
    def number_of_host(self, number_of_host):
        """Sets the number_of_host of this VxmSystemInfo.

        Number of hosts in the cluster  # noqa: E501

        :param number_of_host: The number_of_host of this VxmSystemInfo.  # noqa: E501
        :type: int
        """
        if number_of_host is None:
            raise ValueError("Invalid value for `number_of_host`, must not be `None`")  # noqa: E501

        self._number_of_host = number_of_host

    @property
    def is_external_vc(self):
        """Gets the is_external_vc of this VxmSystemInfo.  # noqa: E501

        Whether the vCenter is an external vCenter  # noqa: E501

        :return: The is_external_vc of this VxmSystemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_external_vc

    @is_external_vc.setter
    def is_external_vc(self, is_external_vc):
        """Sets the is_external_vc of this VxmSystemInfo.

        Whether the vCenter is an external vCenter  # noqa: E501

        :param is_external_vc: The is_external_vc of this VxmSystemInfo.  # noqa: E501
        :type: bool
        """
        if is_external_vc is None:
            raise ValueError("Invalid value for `is_external_vc`, must not be `None`")  # noqa: E501

        self._is_external_vc = is_external_vc

    @property
    def logical_view_status(self):
        """Gets the logical_view_status of this VxmSystemInfo.  # noqa: E501

        Whether the VxRail Manager logical view is enabled  # noqa: E501

        :return: The logical_view_status of this VxmSystemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._logical_view_status

    @logical_view_status.setter
    def logical_view_status(self, logical_view_status):
        """Sets the logical_view_status of this VxmSystemInfo.

        Whether the VxRail Manager logical view is enabled  # noqa: E501

        :param logical_view_status: The logical_view_status of this VxmSystemInfo.  # noqa: E501
        :type: bool
        """
        if logical_view_status is None:
            raise ValueError("Invalid value for `logical_view_status`, must not be `None`")  # noqa: E501

        self._logical_view_status = logical_view_status

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
        if issubclass(VxmSystemInfo, dict):
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
        if not isinstance(other, VxmSystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
