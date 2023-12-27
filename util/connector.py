import httpx
import params

async def make_inference(uploaded_file, patient_id, series_id, model="default"):
    # Attached file
    files = {
        "file": (uploaded_file.name, uploaded_file.read(), "application/x-zip-compressed")
    }
    
    # Patient Data
    data = {
        "patient": patient_id,
        "series": series_id,
        }
    
    # Asynchronously sending a request to the API
    async with httpx.AsyncClient() as client:
        response = await client.post(params.PROD_INFERENCE_V2_API_BASEURL + f"?model={model}", 
                                     data=data, 
                                     files=files, 
                                     timeout=None)
        return response.json()
    
async def get_inference_status(task_id:str):
    # Asynchronously sending a request to the API
    async with httpx.AsyncClient() as client:
        response = await client.get(params.PROD_INFERENCE_STATUS_API_BASEURL + f"/{task_id}", timeout=None)
        return response.json()