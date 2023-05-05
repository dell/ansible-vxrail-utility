# coding: utf-8

"""
    VxRail REST API

    The VxRail REST API provides a programmatic interface for performing VxRail administrative tasks. Data is available in JSON format.  # noqa: E501

    OpenAPI spec version: 1.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vxrail_ansible_utility.api_client import ApiClient


class ESXiHostnameOrManagementIPAddressChangeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_request_get_status(self, request_id_sample_re_hostname, **kwargs):  # noqa: E501
        """v1_request_get_status  # noqa: E501

        Retrieves the operation status and progress report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_request_get_status(request_id_sample_re_hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str request_id_sample_re_hostname: The request ID of any long running operation. (required)
        :return: RequestStatusInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_request_get_status_with_http_info(request_id_sample_re_hostname, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_request_get_status_with_http_info(request_id_sample_re_hostname, **kwargs)  # noqa: E501
            return data

    def v1_request_get_status_with_http_info(self, request_id_sample_re_hostname, **kwargs):  # noqa: E501
        """v1_request_get_status  # noqa: E501

        Retrieves the operation status and progress report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_request_get_status_with_http_info(request_id_sample_re_hostname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str request_id_sample_re_hostname: The request ID of any long running operation. (required)
        :return: RequestStatusInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_id_sample_re_hostname']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_request_get_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_id_sample_re_hostname' is set
        if ('request_id_sample_re_hostname' not in params or
                params['request_id_sample_re_hostname'] is None):
            raise ValueError("Missing the required parameter `request_id_sample_re_hostname` when calling `v1_request_get_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'request_id_sample_re_hostname' in params:
            path_params['requestId_sample_reHostname'] = params['request_id_sample_re_hostname']  # noqa: E501

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
            '/requests/{requestId_sample_reHostname}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RequestStatusInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
