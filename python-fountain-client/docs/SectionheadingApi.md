# swagger_client.SectionheadingApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sectionheading_delete**](SectionheadingApi.md#sectionheading_delete) | **DELETE** /sectionheading | 
[**sectionheading_get**](SectionheadingApi.md#sectionheading_get) | **GET** /sectionheading | 
[**sectionheading_patch**](SectionheadingApi.md#sectionheading_patch) | **PATCH** /sectionheading | 
[**sectionheading_post**](SectionheadingApi.md#sectionheading_post) | **POST** /sectionheading | 

# **sectionheading_delete**
> sectionheading_delete(section_id=section_id, script_id=script_id, text=text, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SectionheadingApi()
section_id = 'section_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.sectionheading_delete(section_id=section_id, script_id=script_id, text=text, prefer=prefer)
except ApiException as e:
    print("Exception when calling SectionheadingApi->sectionheading_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sectionheading_get**
> list[Sectionheading] sectionheading_get(section_id=section_id, script_id=script_id, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SectionheadingApi()
section_id = 'section_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.sectionheading_get(section_id=section_id, script_id=script_id, text=text, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectionheadingApi->sectionheading_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Sectionheading]**](Sectionheading.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sectionheading_patch**
> sectionheading_patch(body=body, prefer=prefer, section_id=section_id, script_id=script_id, text=text)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SectionheadingApi()
body = swagger_client.Sectionheading() # Sectionheading | sectionheading (optional)
prefer = 'prefer_example' # str | Preference (optional)
section_id = 'section_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
text = 'text_example' # str |  (optional)

try:
    api_instance.sectionheading_patch(body=body, prefer=prefer, section_id=section_id, script_id=script_id, text=text)
except ApiException as e:
    print("Exception when calling SectionheadingApi->sectionheading_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sectionheading**](Sectionheading.md)| sectionheading | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **section_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **text** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sectionheading_post**
> sectionheading_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SectionheadingApi()
body = swagger_client.Sectionheading() # Sectionheading | sectionheading (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.sectionheading_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling SectionheadingApi->sectionheading_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sectionheading**](Sectionheading.md)| sectionheading | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **select** | **str**| Filtering Columns | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

