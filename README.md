# Digital Object Recognition
### Description
It is a software solution, based on AI, using computer vision and image processing that detects and defines objects.

This solution allows farmers to optimize time in their production processes. With the recognition of fruits based on their ripe color and counting, the work of packing before sending them for sale is facilitated.

## requirements and main files

|   ***File/req.***    |  **Description**                       |
|---------------|---------------------------------------|
|  `opencv-python`	|  process img-videos to identify objects	|
|  `numpy`	|  operates vectors and matrix				|
|  `flask` |  allows to create n online api|
|  `pillow` |  manipulates images and edition with python	|
|  `gunicorn`	|  allows the app to support multiple requests|
|  `app.py`  |  manage get and post requests in this app	 |
|  `IMGscanner.py`  | manages the selection and identification of objects(based on JSON data)  |

### How to use
1-Please click on "Choose file" button <br />
2-Make sure to upload clear pictures. For a more accurate experience JPG format would be ideal. <br />
3-click on the button "Analyze".

### Important
Use images containing oranges, since the software has been built only to detect oranges(based on color) in farms. 

### Authors
*Faber Ruiz* - [Github](https://github.com/fruizga) || 1196@holbertonschool.com

*Jose Diaz* - [Github](https://github.com/jhosep7) || 1149@holbertonschool.com
