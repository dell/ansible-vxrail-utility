# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class VcenterEmbeddedPSCMigrationSpec(object):
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
        'source_vcsa_host': 'EsxiHostSpec',
        'target_vcsa_host': 'EsxiHostSpec',
        'temporary_ip_setting': 'TemporaryIpSettingSpec'
    }

    attribute_map = {
        'source_vcsa_host': 'source_vcsa_host',
        'target_vcsa_host': 'target_vcsa_host',
        'temporary_ip_setting': 'temporary_ip_setting'
    }

    def __init__(self, source_vcsa_host=None, target_vcsa_host=None, temporary_ip_setting=None):  # noqa: E501
        """VcenterEmbeddedPSCMigrationSpec - a model defined in Swagger"""  # noqa: E501
        self._source_vcsa_host = None
        self._target_vcsa_host = None
        self._temporary_ip_setting = None
        self.discriminator = None
        self.source_vcsa_host = source_vcsa_host
        self.target_vcsa_host = target_vcsa_host
        self.temporary_ip_setting = temporary_ip_setting

    @property
    def source_vcsa_host(self):
        """Gets the source_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501


        :return: The source_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501
        :rtype: EsxiHostSpec
        """
        return self._source_vcsa_host

    @source_vcsa_host.setter
    def source_vcsa_host(self, source_vcsa_host):
        """Sets the source_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.


        :param source_vcsa_host: The source_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501
        :type: EsxiHostSpec
        """
        if source_vcsa_host is None:
            raise ValueError("Invalid value for `source_vcsa_host`, must not be `None`")  # noqa: E501

        self._source_vcsa_host = source_vcsa_host

    @property
    def target_vcsa_host(self):
        """Gets the target_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501


        :return: The target_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501
        :rtype: EsxiHostSpec
        """
        return self._target_vcsa_host

    @target_vcsa_host.setter
    def target_vcsa_host(self, target_vcsa_host):
        """Sets the target_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.


        :param target_vcsa_host: The target_vcsa_host of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501
        :type: EsxiHostSpec
        """
        if target_vcsa_host is None:
            raise ValueError("Invalid value for `target_vcsa_host`, must not be `None`")  # noqa: E501

        self._target_vcsa_host = target_vcsa_host

    @property
    def temporary_ip_setting(self):
        """Gets the temporary_ip_setting of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501


        :return: The temporary_ip_setting of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501
        :rtype: TemporaryIpSettingSpec
        """
        return self._temporary_ip_setting

    @temporary_ip_setting.setter
    def temporary_ip_setting(self, temporary_ip_setting):
        """Sets the temporary_ip_setting of this VcenterEmbeddedPSCMigrationSpec.


        :param temporary_ip_setting: The temporary_ip_setting of this VcenterEmbeddedPSCMigrationSpec.  # noqa: E501
        :type: TemporaryIpSettingSpec
        """
        if temporary_ip_setting is None:
            raise ValueError("Invalid value for `temporary_ip_setting`, must not be `None`")  # noqa: E501

        self._temporary_ip_setting = temporary_ip_setting

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
        if issubclass(VcenterEmbeddedPSCMigrationSpec, dict):
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
        if not isinstance(other, VcenterEmbeddedPSCMigrationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
