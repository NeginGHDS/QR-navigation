

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.server:app", # Python_module_path:FastAPI_instance_name
        host="127.0.0.1", # IP of the api
        port=8000, # port for the api, it is available like-> host:port
        reload=True
    )
