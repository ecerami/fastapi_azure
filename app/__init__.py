import azure.functions as func
from .http_asgi import AsgiMiddleware
import mimesis
from api_app import app


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    fake_user = mimesis.Person()
    return {
        "user_id": user_id,
        "username": fake_user.username(),
        "firstname": fake_user.first_name(),
        "lastname": fake_user.last_name(),
    }


def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)