from pydantic import Field, BaseModel

from api.models import SuccessResponse


class GetExampleResponse(SuccessResponse):
    """Response model to /exemplo_get"""
    exemplo_out: str = Field(...,
                              description="String em upper case.", example="STRING")
    get_message: str = Field("Request GET")


class PostExampleInput(BaseModel):
    """ Post input base model """
    string: exemplo_out: str = Field(...,
                              description="String para ser transformada para upper case.", example="string")
    
    
class PostExampleResponse(SuccessResponse):
    """Response model to /exemplo_post"""
    exemplo_out: str = Field(...,
                              description="String em upper case.", example="STRING")
    post_message: str = Field("Request POST")