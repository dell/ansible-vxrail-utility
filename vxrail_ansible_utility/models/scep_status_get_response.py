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

class ScepStatusGetResponse(object):
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
        'vxm_cert_expire_time': 'str',
        'last_failure_time': 'str',
        'last_error_msg': 'str',
        'last_result': 'str',
        'last_run_time': 'str',
        'last_success_time': 'str',
        'scep_enabled': 'bool'
    }

    attribute_map = {
        'vxm_cert_expire_time': 'vxm_cert_expire_time',
        'last_failure_time': 'last_failure_time',
        'last_error_msg': 'last_error_msg',
        'last_result': 'last_result',
        'last_run_time': 'last_run_time',
        'last_success_time': 'last_success_time',
        'scep_enabled': 'scep_enabled'
    }

    def __init__(self, vxm_cert_expire_time=None, last_failure_time=None, last_error_msg=None, last_result=None, last_run_time=None, last_success_time=None, scep_enabled=None):  # noqa: E501
        """ScepStatusGetResponse - a model defined in Swagger"""  # noqa: E501
        self._vxm_cert_expire_time = None
        self._last_failure_time = None
        self._last_error_msg = None
        self._last_result = None
        self._last_run_time = None
        self._last_success_time = None
        self._scep_enabled = None
        self.discriminator = None
        self.vxm_cert_expire_time = vxm_cert_expire_time
        self.last_failure_time = last_failure_time
        self.last_error_msg = last_error_msg
        self.last_result = last_result
        self.last_run_time = last_run_time
        self.last_success_time = last_success_time
        self.scep_enabled = scep_enabled

    @property
    def vxm_cert_expire_time(self):
        """Gets the vxm_cert_expire_time of this ScepStatusGetResponse.  # noqa: E501

        Expiration time of the VxRail Manager TLS Certificate  # noqa: E501

        :return: The vxm_cert_expire_time of this ScepStatusGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._vxm_cert_expire_time

    @vxm_cert_expire_time.setter
    def vxm_cert_expire_time(self, vxm_cert_expire_time):
        """Sets the vxm_cert_expire_time of this ScepStatusGetResponse.

        Expiration time of the VxRail Manager TLS Certificate  # noqa: E501

        :param vxm_cert_expire_time: The vxm_cert_expire_time of this ScepStatusGetResponse.  # noqa: E501
        :type: str
        """
        if vxm_cert_expire_time is None:
            raise ValueError("Invalid value for `vxm_cert_expire_time`, must not be `None`")  # noqa: E501

        self._vxm_cert_expire_time = vxm_cert_expire_time

    @property
    def last_failure_time(self):
        """Gets the last_failure_time of this ScepStatusGetResponse.  # noqa: E501

        Last failure time of the automated renewal  # noqa: E501

        :return: The last_failure_time of this ScepStatusGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_failure_time

    @last_failure_time.setter
    def last_failure_time(self, last_failure_time):
        """Sets the last_failure_time of this ScepStatusGetResponse.

        Last failure time of the automated renewal  # noqa: E501

        :param last_failure_time: The last_failure_time of this ScepStatusGetResponse.  # noqa: E501
        :type: str
        """
        if last_failure_time is None:
            raise ValueError("Invalid value for `last_failure_time`, must not be `None`")  # noqa: E501

        self._last_failure_time = last_failure_time

    @property
    def last_error_msg(self):
        """Gets the last_error_msg of this ScepStatusGetResponse.  # noqa: E501

        The error message of last failure of the automated renewal  # noqa: E501

        :return: The last_error_msg of this ScepStatusGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_error_msg

    @last_error_msg.setter
    def last_error_msg(self, last_error_msg):
        """Sets the last_error_msg of this ScepStatusGetResponse.

        The error message of last failure of the automated renewal  # noqa: E501

        :param last_error_msg: The last_error_msg of this ScepStatusGetResponse.  # noqa: E501
        :type: str
        """
        if last_error_msg is None:
            raise ValueError("Invalid value for `last_error_msg`, must not be `None`")  # noqa: E501

        self._last_error_msg = last_error_msg

    @property
    def last_result(self):
        """Gets the last_result of this ScepStatusGetResponse.  # noqa: E501

        The status of last automated renewal  # noqa: E501

        :return: The last_result of this ScepStatusGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_result

    @last_result.setter
    def last_result(self, last_result):
        """Sets the last_result of this ScepStatusGetResponse.

        The status of last automated renewal  # noqa: E501

        :param last_result: The last_result of this ScepStatusGetResponse.  # noqa: E501
        :type: str
        """
        if last_result is None:
            raise ValueError("Invalid value for `last_result`, must not be `None`")  # noqa: E501
        allowed_values = ["SUCCESS", "FAILURE", "VXM_CERT_IS_YOUNG"]  # noqa: E501
        if last_result not in allowed_values:
            raise ValueError(
                "Invalid value for `last_result` ({0}), must be one of {1}"  # noqa: E501
                .format(last_result, allowed_values)
            )

        self._last_result = last_result

    @property
    def last_run_time(self):
        """Gets the last_run_time of this ScepStatusGetResponse.  # noqa: E501

        Last run time of the automated renewal  # noqa: E501

        :return: The last_run_time of this ScepStatusGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_run_time

    @last_run_time.setter
    def last_run_time(self, last_run_time):
        """Sets the last_run_time of this ScepStatusGetResponse.

        Last run time of the automated renewal  # noqa: E501

        :param last_run_time: The last_run_time of this ScepStatusGetResponse.  # noqa: E501
        :type: str
        """
        if last_run_time is None:
            raise ValueError("Invalid value for `last_run_time`, must not be `None`")  # noqa: E501

        self._last_run_time = last_run_time

    @property
    def last_success_time(self):
        """Gets the last_success_time of this ScepStatusGetResponse.  # noqa: E501

        Last success time of the automated renewal  # noqa: E501

        :return: The last_success_time of this ScepStatusGetResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_success_time

    @last_success_time.setter
    def last_success_time(self, last_success_time):
        """Sets the last_success_time of this ScepStatusGetResponse.

        Last success time of the automated renewal  # noqa: E501

        :param last_success_time: The last_success_time of this ScepStatusGetResponse.  # noqa: E501
        :type: str
        """
        if last_success_time is None:
            raise ValueError("Invalid value for `last_success_time`, must not be `None`")  # noqa: E501

        self._last_success_time = last_success_time

    @property
    def scep_enabled(self):
        """Gets the scep_enabled of this ScepStatusGetResponse.  # noqa: E501

        The automated renewal is enabled or not  # noqa: E501

        :return: The scep_enabled of this ScepStatusGetResponse.  # noqa: E501
        :rtype: bool
        """
        return self._scep_enabled

    @scep_enabled.setter
    def scep_enabled(self, scep_enabled):
        """Sets the scep_enabled of this ScepStatusGetResponse.

        The automated renewal is enabled or not  # noqa: E501

        :param scep_enabled: The scep_enabled of this ScepStatusGetResponse.  # noqa: E501
        :type: bool
        """
        if scep_enabled is None:
            raise ValueError("Invalid value for `scep_enabled`, must not be `None`")  # noqa: E501

        self._scep_enabled = scep_enabled

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
        if issubclass(ScepStatusGetResponse, dict):
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
        if not isinstance(other, ScepStatusGetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
