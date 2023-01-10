# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.410
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class HostIDRACConfigurationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_hosts_sn_idrac_id_get(self, sn, **kwargs):  # noqa: E501
        """Get a list of iDRAC user slot IDs  # noqa: E501

        Get a list of the available iDRAC user slot IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_id_get(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_hosts_sn_idrac_id_get_with_http_info(sn, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_hosts_sn_idrac_id_get_with_http_info(sn, **kwargs)  # noqa: E501
            return data

    def v1_hosts_sn_idrac_id_get_with_http_info(self, sn, **kwargs):  # noqa: E501
        """Get a list of iDRAC user slot IDs  # noqa: E501

        Get a list of the available iDRAC user slot IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_id_get_with_http_info(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_hosts_sn_idrac_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v1_hosts_sn_idrac_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/hosts/{sn}/idrac/available-user-ids', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_hosts_sn_idrac_network_get(self, sn, **kwargs):  # noqa: E501
        """Get the iDRAC network settings  # noqa: E501

        Get the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_network_get(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: IdracNetworkInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_hosts_sn_idrac_network_get_with_http_info(sn, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_hosts_sn_idrac_network_get_with_http_info(sn, **kwargs)  # noqa: E501
            return data

    def v1_hosts_sn_idrac_network_get_with_http_info(self, sn, **kwargs):  # noqa: E501
        """Get the iDRAC network settings  # noqa: E501

        Get the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_network_get_with_http_info(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: IdracNetworkInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_hosts_sn_idrac_network_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v1_hosts_sn_idrac_network_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/hosts/{sn}/idrac/network', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdracNetworkInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_hosts_sn_idrac_network_patch(self, body, sn, **kwargs):  # noqa: E501
        """Update the iDRAC network settings  # noqa: E501

        Update the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_network_patch(body, sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracNetworkSpec body: The network parameters for the iDRAC network. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_hosts_sn_idrac_network_patch_with_http_info(body, sn, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_hosts_sn_idrac_network_patch_with_http_info(body, sn, **kwargs)  # noqa: E501
            return data

    def v1_hosts_sn_idrac_network_patch_with_http_info(self, body, sn, **kwargs):  # noqa: E501
        """Update the iDRAC network settings  # noqa: E501

        Update the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_network_patch_with_http_info(body, sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracNetworkSpec body: The network parameters for the iDRAC network. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'sn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_hosts_sn_idrac_network_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_hosts_sn_idrac_network_patch`")  # noqa: E501
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v1_hosts_sn_idrac_network_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/hosts/{sn}/idrac/network', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Model202Nocontent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_hosts_sn_idrac_user_get(self, sn, **kwargs):  # noqa: E501
        """Get a list of iDRAC user accounts  # noqa: E501

        Get a list of the iDRAC user accounts on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_user_get(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: list[IdracUserInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_hosts_sn_idrac_user_get_with_http_info(sn, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_hosts_sn_idrac_user_get_with_http_info(sn, **kwargs)  # noqa: E501
            return data

    def v1_hosts_sn_idrac_user_get_with_http_info(self, sn, **kwargs):  # noqa: E501
        """Get a list of iDRAC user accounts  # noqa: E501

        Get a list of the iDRAC user accounts on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_user_get_with_http_info(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: list[IdracUserInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_hosts_sn_idrac_user_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v1_hosts_sn_idrac_user_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/hosts/{sn}/idrac/users', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[IdracUserInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_hosts_sn_idrac_user_id_put(self, body, sn, user_id, **kwargs):  # noqa: E501
        """Update an iDRAC user account  # noqa: E501

        Update an iDRAC user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_user_id_put(body, sn, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracUserUpdateSpec body: The iDRAC user account information for the user to be updated. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :param str user_id: The unique identifier of the iDRAC user. The available range is between 3 and 16. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_hosts_sn_idrac_user_id_put_with_http_info(body, sn, user_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_hosts_sn_idrac_user_id_put_with_http_info(body, sn, user_id, **kwargs)  # noqa: E501
            return data

    def v1_hosts_sn_idrac_user_id_put_with_http_info(self, body, sn, user_id, **kwargs):  # noqa: E501
        """Update an iDRAC user account  # noqa: E501

        Update an iDRAC user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_user_id_put_with_http_info(body, sn, user_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracUserUpdateSpec body: The iDRAC user account information for the user to be updated. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :param str user_id: The unique identifier of the iDRAC user. The available range is between 3 and 16. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'sn', 'user_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_hosts_sn_idrac_user_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_hosts_sn_idrac_user_id_put`")  # noqa: E501
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v1_hosts_sn_idrac_user_id_put`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `v1_hosts_sn_idrac_user_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501
        if 'user_id' in params:
            path_params['userId'] = params['user_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/hosts/{sn}/idrac/users/{userId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Model202Nocontent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_hosts_sn_idrac_user_post(self, body, sn, **kwargs):  # noqa: E501
        """Create an iDRAC user account  # noqa: E501

        Create an iDRAC user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_user_post(body, sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracUserCreateSpec body: The iDRAC user account information for the user to be created. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_hosts_sn_idrac_user_post_with_http_info(body, sn, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_hosts_sn_idrac_user_post_with_http_info(body, sn, **kwargs)  # noqa: E501
            return data

    def v1_hosts_sn_idrac_user_post_with_http_info(self, body, sn, **kwargs):  # noqa: E501
        """Create an iDRAC user account  # noqa: E501

        Create an iDRAC user account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_hosts_sn_idrac_user_post_with_http_info(body, sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracUserCreateSpec body: The iDRAC user account information for the user to be created. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'sn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_hosts_sn_idrac_user_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v1_hosts_sn_idrac_user_post`")  # noqa: E501
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v1_hosts_sn_idrac_user_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/hosts/{sn}/idrac/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Model202Nocontent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_hosts_sn_idrac_network_get(self, sn, **kwargs):  # noqa: E501
        """Get the iDRAC network settings  # noqa: E501

        Get the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_hosts_sn_idrac_network_get(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: IdracNetworkInfoWithIPv6
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_hosts_sn_idrac_network_get_with_http_info(sn, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_hosts_sn_idrac_network_get_with_http_info(sn, **kwargs)  # noqa: E501
            return data

    def v2_hosts_sn_idrac_network_get_with_http_info(self, sn, **kwargs):  # noqa: E501
        """Get the iDRAC network settings  # noqa: E501

        Get the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_hosts_sn_idrac_network_get_with_http_info(sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sn: The serial number of the host to be queried. (required)
        :return: IdracNetworkInfoWithIPv6
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_hosts_sn_idrac_network_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v2_hosts_sn_idrac_network_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/hosts/{sn}/idrac/network', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdracNetworkInfoWithIPv6',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_hosts_sn_idrac_network_patch(self, body, sn, **kwargs):  # noqa: E501
        """Update the iDRAC network settings  # noqa: E501

        Update the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_hosts_sn_idrac_network_patch(body, sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracNetworkIPv6Spec body: The network parameters for the iDRAC network. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_hosts_sn_idrac_network_patch_with_http_info(body, sn, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_hosts_sn_idrac_network_patch_with_http_info(body, sn, **kwargs)  # noqa: E501
            return data

    def v2_hosts_sn_idrac_network_patch_with_http_info(self, body, sn, **kwargs):  # noqa: E501
        """Update the iDRAC network settings  # noqa: E501

        Update the iDRAC network settings on the specified host.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_hosts_sn_idrac_network_patch_with_http_info(body, sn, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IdracNetworkIPv6Spec body: The network parameters for the iDRAC network. (required)
        :param str sn: The serial number of the host to be queried. (required)
        :return: Model202Nocontent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'sn']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_hosts_sn_idrac_network_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `v2_hosts_sn_idrac_network_patch`")  # noqa: E501
        # verify the required parameter 'sn' is set
        if ('sn' not in params or
                params['sn'] is None):
            raise ValueError("Missing the required parameter `sn` when calling `v2_hosts_sn_idrac_network_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sn' in params:
            path_params['sn'] = params['sn']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/v2/hosts/{sn}/idrac/network', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Model202Nocontent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
