# spline-api
### A api to draw spline


## Usage
- Clone this project
- Create and active cirtual envirement
    ```
    virtualenv venv
    source venv/bin/activate
    ```
- Install requirements
    `pip install -r requirements.txt`

- Run server
    `python app.py`

- Make post request to server with **multipart/form-data** Content-Type Header and **tck** and **image** body
    tck structure example:
    ```
    [
        [0, 0, 0, 0, 0.68247947, 1, 1, 1, 1],
        [
            [150, 44.395705, 1279.960176, 94.6343365, 300],
            [150, 2446.74514, 1017.743452, -18.844085, 700]
        ],
        3
    ]
    ```
    request example:
    ```
    curl --request POST \
  --url http://127.0.0.1:5000/ \
  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
  --form 'tck=[
    [0, 0, 0, 0, 0.68247947, 1, 1, 1, 1],
    [
        [150, 44.395705, 1279.960176, 94.6343365, 300],
        [150, 2446.74514, 1017.743452, -18.844085, 700]
    ],
    3
    ]' \
  --form image=image.jpg --output response.png
    ```
    it return an image as response.
