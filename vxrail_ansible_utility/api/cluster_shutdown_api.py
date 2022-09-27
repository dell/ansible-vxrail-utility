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


class ClusterShutdownApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_cluster_shutdown_post(self, **kwargs):  # noqa: E501
        """Shut down a cluster or perform a shutdown dry run  # noqa: E501

        Shut down a cluster or perform a shutdown dry run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_cluster_shutdown_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterShutdownBody body: Perform an optional dry run to check whether it is safe to shut down. The default value is false.
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_cluster_shutdown_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_cluster_shutdown_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_cluster_shutdown_post_with_http_info(self, **kwargs):  # noqa: E501
        """Shut down a cluster or perform a shutdown dry run  # noqa: E501

        Shut down a cluster or perform a shutdown dry run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_cluster_shutdown_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ClusterShutdownBody body: Perform an optional dry run to check whether it is safe to shut down. The default value is false.
        :return: InlineResponse202
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_cluster_shutdown_post" % key
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
            '/v1/cluster/shutdown', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse202',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
