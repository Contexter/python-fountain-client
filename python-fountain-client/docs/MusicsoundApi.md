# swagger_client.MusicsoundApi

All URIs are relative to *https://restapi.benedikt-eickhoff.de/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**musicsound_delete**](MusicsoundApi.md#musicsound_delete) | **DELETE** /musicsound | 
[**musicsound_get**](MusicsoundApi.md#musicsound_get) | **GET** /musicsound | 
[**musicsound_patch**](MusicsoundApi.md#musicsound_patch) | **PATCH** /musicsound | 
[**musicsound_post**](MusicsoundApi.md#musicsound_post) | **POST** /musicsound | 

# **musicsound_delete**
> musicsound_delete(music_sound_id=music_sound_id, scene_id=scene_id, cue=cue, description=description, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MusicsoundApi()
music_sound_id = 'music_sound_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
cue = 'cue_example' # str |  (optional)
description = 'description_example' # str |  (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_instance.musicsound_delete(music_sound_id=music_sound_id, scene_id=scene_id, cue=cue, description=description, prefer=prefer)
except ApiException as e:
    print("Exception when calling MusicsoundApi->musicsound_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **music_sound_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **cue** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **musicsound_get**
> list[Musicsound] musicsound_get(music_sound_id=music_sound_id, scene_id=scene_id, cue=cue, description=description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MusicsoundApi()
music_sound_id = 'music_sound_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
cue = 'cue_example' # str |  (optional)
description = 'description_example' # str |  (optional)
select = 'select_example' # str | Filtering Columns (optional)
order = 'order_example' # str | Ordering (optional)
range = 'range_example' # str | Limiting and Pagination (optional)
range_unit = 'items' # str | Limiting and Pagination (optional) (default to items)
offset = 'offset_example' # str | Limiting and Pagination (optional)
limit = 'limit_example' # str | Limiting and Pagination (optional)
prefer = 'prefer_example' # str | Preference (optional)

try:
    api_response = api_instance.musicsound_get(music_sound_id=music_sound_id, scene_id=scene_id, cue=cue, description=description, select=select, order=order, range=range, range_unit=range_unit, offset=offset, limit=limit, prefer=prefer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MusicsoundApi->musicsound_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **music_sound_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **cue** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **select** | **str**| Filtering Columns | [optional] 
 **order** | **str**| Ordering | [optional] 
 **range** | **str**| Limiting and Pagination | [optional] 
 **range_unit** | **str**| Limiting and Pagination | [optional] [default to items]
 **offset** | **str**| Limiting and Pagination | [optional] 
 **limit** | **str**| Limiting and Pagination | [optional] 
 **prefer** | **str**| Preference | [optional] 

### Return type

[**list[Musicsound]**](Musicsound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **musicsound_patch**
> musicsound_patch(body=body, prefer=prefer, music_sound_id=music_sound_id, scene_id=scene_id, cue=cue, description=description)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MusicsoundApi()
body = swagger_client.Musicsound() # Musicsound | musicsound (optional)
prefer = 'prefer_example' # str | Preference (optional)
music_sound_id = 'music_sound_id_example' # str |  (optional)
scene_id = 'scene_id_example' # str |  (optional)
cue = 'cue_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    api_instance.musicsound_patch(body=body, prefer=prefer, music_sound_id=music_sound_id, scene_id=scene_id, cue=cue, description=description)
except ApiException as e:
    print("Exception when calling MusicsoundApi->musicsound_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Musicsound**](Musicsound.md)| musicsound | [optional] 
 **prefer** | **str**| Preference | [optional] 
 **music_sound_id** | **str**|  | [optional] 
 **scene_id** | **str**|  | [optional] 
 **cue** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.pgrst.object+json;nulls=stripped, application/vnd.pgrst.object+json, text/csv
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **musicsound_post**
> musicsound_post(body=body, prefer=prefer, select=select)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MusicsoundApi()
body = swagger_client.Musicsound() # Musicsound | musicsound (optional)
prefer = 'prefer_example' # str | Preference (optional)
select = 'select_example' # str | Filtering Columns (optional)

try:
    api_instance.musicsound_post(body=body, prefer=prefer, select=select)
except ApiException as e:
    print("Exception when calling MusicsoundApi->musicsound_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Musicsound**](Musicsound.md)| musicsound | [optional] 
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

