# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 7.0.400
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class ChassisInformationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_chassis_get(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v1)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_chassis_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_chassis_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_chassis_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_chassis_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v1)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_chassis_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_chassis_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v1/chassis', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChassisInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_chassis_id_get(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v1)  # noqa: E501

        Get information about a user-specified VxRail chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_chassis_id_get(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: The chassis ID for the VxRail chassis you want to query. (required)
        :return: ChassisInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
            return data

    def v1_chassis_id_get_with_http_info(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v1)  # noqa: E501

        Get information about a user-specified VxRail chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_chassis_id_get_with_http_info(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: The chassis ID for the VxRail chassis you want to query. (required)
        :return: ChassisInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chassis_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_chassis_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chassis_id' is set
        if ('chassis_id' not in params or
                params['chassis_id'] is None):
            raise ValueError("Missing the required parameter `chassis_id` when calling `v1_chassis_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chassis_id' in params:
            path_params['chassis_id'] = params['chassis_id']  # noqa: E501

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
            '/v1/chassis/{chassis_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChassisInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_chassis_get(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v2)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis. Version v2 contains the same attributes as the v1 version plus a geo-location attribute in HostBasicInfoV2.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_chassis_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfoV2]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_chassis_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_chassis_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_chassis_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v2)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis. Version v2 contains the same attributes as the v1 version plus a geo-location attribute in HostBasicInfoV2.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_chassis_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfoV2]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_chassis_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v2/chassis', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChassisInfoV2]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_chassis_id_get(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v2)  # noqa: E501

        Get information about the user-specified VxRail chassis. Version v2 contains the same attributes as the v1 version plus a geo-location attribute in HostBasicInfoV2.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_chassis_id_get(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: The chassis ID for the VxRail chassis you want to query. (required)
        :return: ChassisInfoV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
            return data

    def v2_chassis_id_get_with_http_info(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v2)  # noqa: E501

        Get information about the user-specified VxRail chassis. Version v2 contains the same attributes as the v1 version plus a geo-location attribute in HostBasicInfoV2.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_chassis_id_get_with_http_info(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: The chassis ID for the VxRail chassis you want to query. (required)
        :return: ChassisInfoV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chassis_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_chassis_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chassis_id' is set
        if ('chassis_id' not in params or
                params['chassis_id'] is None):
            raise ValueError("Missing the required parameter `chassis_id` when calling `v2_chassis_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chassis_id' in params:
            path_params['chassis_id'] = params['chassis_id']  # noqa: E501

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
            '/v2/chassis/{chassis_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChassisInfoV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v3_chassis_get(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v3)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_chassis_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfoV3]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v3_chassis_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v3_chassis_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v3_chassis_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v3)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_chassis_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfoV3]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_chassis_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v3/chassis', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChassisInfoV3]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v3_chassis_id_get(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v3)  # noqa: E501

        Get information about the user-specified VxRail chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_chassis_id_get(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: Chassis ID (required)
        :return: ChassisInfoV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v3_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v3_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
            return data

    def v3_chassis_id_get_with_http_info(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v3)  # noqa: E501

        Get information about the user-specified VxRail chassis.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v3_chassis_id_get_with_http_info(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: Chassis ID (required)
        :return: ChassisInfoV3
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chassis_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v3_chassis_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chassis_id' is set
        if ('chassis_id' not in params or
                params['chassis_id'] is None):
            raise ValueError("Missing the required parameter `chassis_id` when calling `v3_chassis_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chassis_id' in params:
            path_params['chassis_id'] = params['chassis_id']  # noqa: E501

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
            '/v3/chassis/{chassis_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChassisInfoV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v4_chassis_get(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v4)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis. The V4 version adds support for satellite nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v4_chassis_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfoV4]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v4_chassis_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v4_chassis_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v4_chassis_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of VxRail chassis (v4)  # noqa: E501

        Retrieve a list of VxRail chassis and information about the nodes in each chassis. The V4 version adds support for satellite nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v4_chassis_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ChassisInfoV4]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v4_chassis_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/v4/chassis', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChassisInfoV4]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v4_chassis_id_get(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v4)  # noqa: E501

        Get information about the user-specified VxRail chassis. V4 version adds support for satellite nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v4_chassis_id_get(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: Chassis ID (required)
        :return: ChassisInfoV4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v4_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v4_chassis_id_get_with_http_info(chassis_id, **kwargs)  # noqa: E501
            return data

    def v4_chassis_id_get_with_http_info(self, chassis_id, **kwargs):  # noqa: E501
        """Get information about a user-specified chassis (v4)  # noqa: E501

        Get information about the user-specified VxRail chassis. V4 version adds support for satellite nodes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v4_chassis_id_get_with_http_info(chassis_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str chassis_id: Chassis ID (required)
        :return: ChassisInfoV4
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['chassis_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v4_chassis_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'chassis_id' is set
        if ('chassis_id' not in params or
                params['chassis_id'] is None):
            raise ValueError("Missing the required parameter `chassis_id` when calling `v4_chassis_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'chassis_id' in params:
            path_params['chassis_id'] = params['chassis_id']  # noqa: E501

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
            '/v4/chassis/{chassis_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChassisInfoV4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
