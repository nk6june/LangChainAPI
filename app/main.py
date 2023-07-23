from fastapi import FastAPI
from langcorn import create_service
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from conversation import conversation


class Input(BaseModel):
    """
    Input model for the conversation endpoint.
    """
    human_input: str

class Output(BaseModel):
    """
    Output model for the conversation endpoint.
    """
    output: str

app = FastAPI()

@app.post("/conversation")
async def input(input: Input):
    """
    Endpoint to carry out a conversation with the LangCorn service.

    Parameters:
        - input (Input): Input model containing the user's message.

    Returns:
        Output: Output model containing LangCorn's response.
    """
    output = Output(output=conversation(input.human_input))
    return output

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
