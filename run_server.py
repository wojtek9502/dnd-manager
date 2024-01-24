import uvicorn


def run_server():
    uvicorn.run("app:app", host='0.0.0.0', port=8080)


if __name__ == '__main__':
    run_server()
