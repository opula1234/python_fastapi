from fastapi import FastAPI

app = FastAPI(
    title="Simple FastAPI Application",
    description="This API provides two endpoints: one for a root message and another for a welcome message.",
    version="1.0.0"
)
"""
This module creates a simple FastAPI application with two endpoints:
- GET /: Returns a message directing users to the documentation page.
- GET /welcome: Returns a welcome message.
"""


@app.get(
    "/",
    tags=["Root"],
    summary="Root endpoint",
    description="Returns a message directing users to the documentation page."
)
def initial_root():
    """
    Root endpoint that returns a message directing users to the docs page.
    """
    return {"msg": "Please visit docs page for documentations..."}


@app.get(
    "/welcome",
    tags=["Welcome"],
    summary="Welcome endpoint",
    description="Returns a welcome message."
)
def welcome_message():
    """
    Welcome endpoint that returns a welcome message.
    """
    return {"msg": "Welcome to FastAPI"}


@app.get("/welcome_user")
def greet_user():
    return {"Msg": "Thanks for coming"}
