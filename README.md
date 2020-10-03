# Image Processing
## Overview
The WordpressImagePrepare tool executes the following tasks
- Renaming according to directory name
- Meta data cleaning to a configurable value
- Resizing and Cropping according to configurable format
## Requirements
Folder naming is expected in the form *foo_bar*, *foo-bar* or *fooBar* and not *foo bar*.
## Usage
<code>WordpressImagePrepare [options] [files]</code>
<code>find Gallery -type f | xargs python3 src/main.py
</code>
### Examples
### Options:
#### -c: config file
provide config file in the form:  
<code>{<br/>
  "size": [2000 , 1500],<br/>
  "datetime": "2000:00:00 00:00:00",<br/>
  "gps_altitude": 8848.0,<br/>
  "gps_latitude": [19.0, 16.0, 46.6464],<br/>
  "gps_longitude": [166.0, 38.0, 53.0124]<br/>
}</code>  
Per default the above config will be used
#### -m override metadata
#### -r resize and crop image
## Dependencies