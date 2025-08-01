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

class ReportComponentContent(object):
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
        'label': 'str',
        'kgs_result': 'str',
        'expect_kgs_result': 'str',
        'version': 'str',
        'build': 'str',
        'type': 'str',
        'versions_supported': 'ReportComponentVersionSupported',
        'expect_version': 'str',
        'expect_build': 'str'
    }

    attribute_map = {
        'label': 'label',
        'kgs_result': 'kgs_result',
        'expect_kgs_result': 'expect_kgs_result',
        'version': 'version',
        'build': 'build',
        'type': 'type',
        'versions_supported': 'versions_supported',
        'expect_version': 'expect_version',
        'expect_build': 'expect_build'
    }

    def __init__(self, label=None, kgs_result=None, expect_kgs_result=None, version=None, build=None, type=None, versions_supported=None, expect_version=None, expect_build=None):  # noqa: E501
        """ReportComponentContent - a model defined in Swagger"""  # noqa: E501
        self._label = None
        self._kgs_result = None
        self._expect_kgs_result = None
        self._version = None
        self._build = None
        self._type = None
        self._versions_supported = None
        self._expect_version = None
        self._expect_build = None
        self.discriminator = None
        if label is not None:
            self.label = label
        if kgs_result is not None:
            self.kgs_result = kgs_result
        if expect_kgs_result is not None:
            self.expect_kgs_result = expect_kgs_result
        if version is not None:
            self.version = version
        if build is not None:
            self.build = build
        if type is not None:
            self.type = type
        if versions_supported is not None:
            self.versions_supported = versions_supported
        if expect_version is not None:
            self.expect_version = expect_version
        if expect_build is not None:
            self.expect_build = expect_build

    @property
    def label(self):
        """Gets the label of this ReportComponentContent.  # noqa: E501


        :return: The label of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ReportComponentContent.


        :param label: The label of this ReportComponentContent.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def kgs_result(self):
        """Gets the kgs_result of this ReportComponentContent.  # noqa: E501


        :return: The kgs_result of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._kgs_result

    @kgs_result.setter
    def kgs_result(self, kgs_result):
        """Sets the kgs_result of this ReportComponentContent.


        :param kgs_result: The kgs_result of this ReportComponentContent.  # noqa: E501
        :type: str
        """

        self._kgs_result = kgs_result

    @property
    def expect_kgs_result(self):
        """Gets the expect_kgs_result of this ReportComponentContent.  # noqa: E501


        :return: The expect_kgs_result of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._expect_kgs_result

    @expect_kgs_result.setter
    def expect_kgs_result(self, expect_kgs_result):
        """Sets the expect_kgs_result of this ReportComponentContent.


        :param expect_kgs_result: The expect_kgs_result of this ReportComponentContent.  # noqa: E501
        :type: str
        """

        self._expect_kgs_result = expect_kgs_result

    @property
    def version(self):
        """Gets the version of this ReportComponentContent.  # noqa: E501


        :return: The version of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReportComponentContent.


        :param version: The version of this ReportComponentContent.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def build(self):
        """Gets the build of this ReportComponentContent.  # noqa: E501


        :return: The build of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this ReportComponentContent.


        :param build: The build of this ReportComponentContent.  # noqa: E501
        :type: str
        """

        self._build = build

    @property
    def type(self):
        """Gets the type of this ReportComponentContent.  # noqa: E501


        :return: The type of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportComponentContent.


        :param type: The type of this ReportComponentContent.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "SOFTWARE", "vSAN", "BIOS", "HBA", "NIC", "iDRAC", "BOSS", "SATADOM", "M2", "iSM", "iDSDM", "BACK_PLANE", "PM", "DEVICE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def versions_supported(self):
        """Gets the versions_supported of this ReportComponentContent.  # noqa: E501


        :return: The versions_supported of this ReportComponentContent.  # noqa: E501
        :rtype: ReportComponentVersionSupported
        """
        return self._versions_supported

    @versions_supported.setter
    def versions_supported(self, versions_supported):
        """Sets the versions_supported of this ReportComponentContent.


        :param versions_supported: The versions_supported of this ReportComponentContent.  # noqa: E501
        :type: ReportComponentVersionSupported
        """

        self._versions_supported = versions_supported

    @property
    def expect_version(self):
        """Gets the expect_version of this ReportComponentContent.  # noqa: E501


        :return: The expect_version of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._expect_version

    @expect_version.setter
    def expect_version(self, expect_version):
        """Sets the expect_version of this ReportComponentContent.


        :param expect_version: The expect_version of this ReportComponentContent.  # noqa: E501
        :type: str
        """

        self._expect_version = expect_version

    @property
    def expect_build(self):
        """Gets the expect_build of this ReportComponentContent.  # noqa: E501


        :return: The expect_build of this ReportComponentContent.  # noqa: E501
        :rtype: str
        """
        return self._expect_build

    @expect_build.setter
    def expect_build(self, expect_build):
        """Sets the expect_build of this ReportComponentContent.


        :param expect_build: The expect_build of this ReportComponentContent.  # noqa: E501
        :type: str
        """

        self._expect_build = expect_build

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
        if issubclass(ReportComponentContent, dict):
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
        if not isinstance(other, ReportComponentContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
