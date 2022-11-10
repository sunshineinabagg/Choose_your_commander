import uvicorn

uvicorn.run(
    'svc.app:app',
    reload=True
)