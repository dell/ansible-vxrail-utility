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

class VxMCsrSpec(object):
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
        'country': 'str',
        'state': 'str',
        'locality': 'str',
        'organization': 'str',
        'organization_unit': 'str',
        'common_name': 'str',
        'email_address': 'str',
        'subject_alt_name': 'list[str]'
    }

    attribute_map = {
        'country': 'country',
        'state': 'state',
        'locality': 'locality',
        'organization': 'organization',
        'organization_unit': 'organization_unit',
        'common_name': 'common_name',
        'email_address': 'email_address',
        'subject_alt_name': 'subject_alt_name'
    }

    def __init__(self, country=None, state=None, locality=None, organization=None, organization_unit=None, common_name=None, email_address=None, subject_alt_name=None):  # noqa: E501
        """VxMCsrSpec - a model defined in Swagger"""  # noqa: E501
        self._country = None
        self._state = None
        self._locality = None
        self._organization = None
        self._organization_unit = None
        self._common_name = None
        self._email_address = None
        self._subject_alt_name = None
        self.discriminator = None
        self.country = country
        if state is not None:
            self.state = state
        self.locality = locality
        self.organization = organization
        self.organization_unit = organization_unit
        self.common_name = common_name
        if email_address is not None:
            self.email_address = email_address
        if subject_alt_name is not None:
            self.subject_alt_name = subject_alt_name

    @property
    def country(self):
        """Gets the country of this VxMCsrSpec.  # noqa: E501

        The two letter country code.  # noqa: E501

        :return: The country of this VxMCsrSpec.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this VxMCsrSpec.

        The two letter country code.  # noqa: E501

        :param country: The country of this VxMCsrSpec.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def state(self):
        """Gets the state of this VxMCsrSpec.  # noqa: E501

        The state or province name.  # noqa: E501

        :return: The state of this VxMCsrSpec.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VxMCsrSpec.

        The state or province name.  # noqa: E501

        :param state: The state of this VxMCsrSpec.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def locality(self):
        """Gets the locality of this VxMCsrSpec.  # noqa: E501

        The locality name.  # noqa: E501

        :return: The locality of this VxMCsrSpec.  # noqa: E501
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """Sets the locality of this VxMCsrSpec.

        The locality name.  # noqa: E501

        :param locality: The locality of this VxMCsrSpec.  # noqa: E501
        :type: str
        """
        if locality is None:
            raise ValueError("Invalid value for `locality`, must not be `None`")  # noqa: E501

        self._locality = locality

    @property
    def organization(self):
        """Gets the organization of this VxMCsrSpec.  # noqa: E501

        The organization name.  # noqa: E501

        :return: The organization of this VxMCsrSpec.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this VxMCsrSpec.

        The organization name.  # noqa: E501

        :param organization: The organization of this VxMCsrSpec.  # noqa: E501
        :type: str
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def organization_unit(self):
        """Gets the organization_unit of this VxMCsrSpec.  # noqa: E501

        The organization unit name.  # noqa: E501

        :return: The organization_unit of this VxMCsrSpec.  # noqa: E501
        :rtype: str
        """
        return self._organization_unit

    @organization_unit.setter
    def organization_unit(self, organization_unit):
        """Sets the organization_unit of this VxMCsrSpec.

        The organization unit name.  # noqa: E501

        :param organization_unit: The organization_unit of this VxMCsrSpec.  # noqa: E501
        :type: str
        """
        if organization_unit is None:
            raise ValueError("Invalid value for `organization_unit`, must not be `None`")  # noqa: E501

        self._organization_unit = organization_unit

    @property
    def common_name(self):
        """Gets the common_name of this VxMCsrSpec.  # noqa: E501

        The common name.  # noqa: E501

        :return: The common_name of this VxMCsrSpec.  # noqa: E501
        :rtype: str
        """
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        """Sets the common_name of this VxMCsrSpec.

        The common name.  # noqa: E501

        :param common_name: The common_name of this VxMCsrSpec.  # noqa: E501
        :type: str
        """
        if common_name is None:
            raise ValueError("Invalid value for `common_name`, must not be `None`")  # noqa: E501

        self._common_name = common_name

    @property
    def email_address(self):
        """Gets the email_address of this VxMCsrSpec.  # noqa: E501

        The email address.  # noqa: E501

        :return: The email_address of this VxMCsrSpec.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this VxMCsrSpec.

        The email address.  # noqa: E501

        :param email_address: The email_address of this VxMCsrSpec.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def subject_alt_name(self):
        """Gets the subject_alt_name of this VxMCsrSpec.  # noqa: E501

        Specify the IP addresses or domains as the alternate names.  # noqa: E501

        :return: The subject_alt_name of this VxMCsrSpec.  # noqa: E501
        :rtype: list[str]
        """
        return self._subject_alt_name

    @subject_alt_name.setter
    def subject_alt_name(self, subject_alt_name):
        """Sets the subject_alt_name of this VxMCsrSpec.

        Specify the IP addresses or domains as the alternate names.  # noqa: E501

        :param subject_alt_name: The subject_alt_name of this VxMCsrSpec.  # noqa: E501
        :type: list[str]
        """

        self._subject_alt_name = subject_alt_name

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
        if issubclass(VxMCsrSpec, dict):
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
        if not isinstance(other, VxMCsrSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
