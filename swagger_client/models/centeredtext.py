# coding: utf-8

"""
    standard public schema

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 12.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Centeredtext(object):
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
        'centered_id': 'int',
        'script_id': 'int',
        'text': 'str'
    }

    attribute_map = {
        'centered_id': 'centered_id',
        'script_id': 'script_id',
        'text': 'text'
    }

    def __init__(self, centered_id=None, script_id=None, text=None):  # noqa: E501
        """Centeredtext - a model defined in Swagger"""  # noqa: E501
        self._centered_id = None
        self._script_id = None
        self._text = None
        self.discriminator = None
        self.centered_id = centered_id
        if script_id is not None:
            self.script_id = script_id
        if text is not None:
            self.text = text

    @property
    def centered_id(self):
        """Gets the centered_id of this Centeredtext.  # noqa: E501

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :return: The centered_id of this Centeredtext.  # noqa: E501
        :rtype: int
        """
        return self._centered_id

    @centered_id.setter
    def centered_id(self, centered_id):
        """Sets the centered_id of this Centeredtext.

        Note: This is a Primary Key.<pk/>  # noqa: E501

        :param centered_id: The centered_id of this Centeredtext.  # noqa: E501
        :type: int
        """
        if centered_id is None:
            raise ValueError("Invalid value for `centered_id`, must not be `None`")  # noqa: E501

        self._centered_id = centered_id

    @property
    def script_id(self):
        """Gets the script_id of this Centeredtext.  # noqa: E501

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :return: The script_id of this Centeredtext.  # noqa: E501
        :rtype: int
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this Centeredtext.

        Note: This is a Foreign Key to `script.script_id`.<fk table='script' column='script_id'/>  # noqa: E501

        :param script_id: The script_id of this Centeredtext.  # noqa: E501
        :type: int
        """

        self._script_id = script_id

    @property
    def text(self):
        """Gets the text of this Centeredtext.  # noqa: E501


        :return: The text of this Centeredtext.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Centeredtext.


        :param text: The text of this Centeredtext.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(Centeredtext, dict):
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
        if not isinstance(other, Centeredtext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other