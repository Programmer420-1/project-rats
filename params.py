import os 
DEV_INFERENCE_API_BASEURL = "http://localhost:8000/infer"
DEV_INFERENCE_V2_API_BASEURL = "http://localhost:8000/v2/infer"
DEV_TEST_INFERENCE_API_BASEURL = "http://localhost:8000/infer_test"

DEV_INFERENCE_STATUS_API_BASEURL = "http://localhost:8000/inference/status"

PROD_INFERENCE_API_BASEURL = "http://34.30.94.255:8000/infer"
PROD_INFERENCE_V2_API_BASEURL = "http://34.30.94.255:8000/v2/infer"
PROD_TEST_INFERENCE_API_BASEURL = "http://34.30.94.255:8000/infer_test"

PROD_INFERENCE_STATUS_API_BASEURL = "http://34.30.94.255:8000/inference/status"

MODEL_CHOICE = ('default', 'finetuned')

GLOBAL_CSS = os.path.join('static', 'styles', 'global.css')
OVERVIEW_CSS = os.path.join('static', 'styles', 'overview.css')
MODEL_LAB_CSS = os.path.join('static', 'styles', 'model_lab.css')

DEBUG = False
