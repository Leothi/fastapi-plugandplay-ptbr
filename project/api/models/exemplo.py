from pydantic import Field, BaseModel

from api.models import SuccessResponse


class GetExampleResponse(SuccessResponse):
    """Response model to /get"""
    exemplo_out: str = Field(...,
                             description="String em upper case.", example="STRING")
    get_message: str = Field("Request de exemplo GET.",
                              description="Mensagem de exemplo.",
                              example="Request de exemplo GET.")


class PostExampleInput(BaseModel):
    """ Post input base model """
    string: str = Field(..., description="String para ser transformada para upper case.", example="string")


class PostExampleResponse(SuccessResponse):
    """Response model to /post"""
    exemplo_out: str = Field(...,
                             description="String em upper case.", example="STRING")
    post_message: str = Field("Request de exemplo POST.",
                              description="Mensagem de exemplo.",
                              example="Request de exemplo POST.")

