# swagger_client.RevisionhistoryApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revisionhistory_delete**](RevisionhistoryApi.md#revisionhistory_delete) | **DELETE** /revisionhistory | 
[**revisionhistory_get**](RevisionhistoryApi.md#revisionhistory_get) | **GET** /revisionhistory | 
[**revisionhistory_patch**](RevisionhistoryApi.md#revisionhistory_patch) | **PATCH** /revisionhistory | 
[**revisionhistory_post**](RevisionhistoryApi.md#revisionhistory_post) | **POST** /revisionhistory | 

# **revisionhistory_delete**
> revisionhistory_delete(revision_id=revision_id, script_id=script_id, _date=_date, change_description=change_description, editor=editor, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevisionhistoryApi()
revision_id = 'revision_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
_date = '2013-10-20' # date |  (optional)
change_description = 'change_description_example' # str |  (optional)
editor = 'editor_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.revisionhistory_delete(revision_id=revision_id, script_id=script_id, _date=_date, change_description=change_description, editor=editor, prefer=prefer)
except ApiException as e:
    print("Exception when calling RevisionhistoryApi->revisionhistory_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revision_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **_date** | **date**|  | [optional] 
 **change_description** | **str**|  | [optional] 
 **editor** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revisionhistory_get**
> list[Revisionhistory] revisionhistory_get(revision_id=revision_id, script_id=script_id, _date=_date, change_description=change_description, editor=editor, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevisionhistoryApi()
revision_id = 'revision_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
_date = '2013-10-20' # date |  (optional)
change_description = 'change_description_example' # str |  (optional)
editor = 'editor_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.revisionhistory_get(revision_id=revision_id, script_id=script_id, _date=_date, change_description=change_description, editor=editor, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevisionhistoryApi->revisionhistory_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revision_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **_date** | **date**|  | [optional] 
 **change_description** | **str**|  | [optional] 
 **editor** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Revisionhistory]**](Revisionhistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revisionhistory_patch**
> revisionhistory_patch(body=body, prefer=prefer, revision_id=revision_id, script_id=script_id, _date=_date, change_description=change_description, editor=editor)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevisionhistoryApi()
body = swagger_client.Revisionhistory() # Revisionhistory | revisionhistory (optional)
prefer = 'prefer_example' # str | Preference (optional)
revision_id = 'revision_id_example' # str |  (optional)
script_id = 'script_id_example' # str |  (optional)
_date = '2013-10-20' # date |  (optional)
change_description = 'change_description_example' # str |  (optional)
editor = 'editor_example' # str |  (optional)

try:
    api_instance.revisionhistory_patch(body=body, prefer=prefer, revision_id=revision_id, script_id=script_id, _date=_date, change_description=change_description, editor=editor)
except ApiException as e:
    print("Exception when calling RevisionhistoryApi->revisionhistory_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Revisionhistory**](Revisionhistory.md)| revisionhistory | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **revision_id** | **str**|  | [optional] 
 **script_id** | **str**|  | [optional] 
 **_date** | **date**|  | [optional] 
 **change_description** | **str**|  | [optional] 
 **editor** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revisionhistory_post**
> revisionhistory_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RevisionhistoryApi()
body = swagger_client.Revisionhistory() # Revisionhistory | revisionhistory (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.revisionhistory_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling RevisionhistoryApi->revisionhistory_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Revisionhistory**](Revisionhistory.md)| revisionhistory | [optional] 
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

