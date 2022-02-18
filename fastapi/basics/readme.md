# FASTAPI BASICS
![Build Passed](https://img.shields.io/badge/BUILD-PASSED-<green>.svg)

FastAPI is a modern, python-based high-performance web framework used to create Rest APIs. Its key features are that is fast, up to 300% faster to code, fewer bugs, easy to use, and production-friendly.


## 🧰 Languages and Tools

![Made withJupyter](https://img.shields.io/badge/Made%20with-Python-red?style=for-the-badge&logo=Python&logoColor=ffdd54)![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/Naereen/badges) 

## ✍ Commands Used
### Installation
```
pip install fastapi

pip install uvicorn

```
### Running the App
Navigate to the main.py’s folder and run this command
```
uvicorn main:app --reload

```
## Advantages

FastAPI provides us automatically with SwaggerUI which is a genius and very helpful UI that allows us to visualize and interact with the API’s resources. It can also be used for testing even for POST APIs used in the code. You can access it by adding the /docs in your APIs URL.

```
http://127.0.0.1:8000/docs

```