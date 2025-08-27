import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Log handled exceptions
        logger.warning(f"Handled exception: {exc} | Context: {context}")
        response.data = {
            "success": False,
            "message": str(response.data.get("detail", "An error occurred")),
            "errors": response.data if "detail" not in response.data else None,
        }
    else:
        # Log unhandled exceptions
        logger.error(f"Unhandled exception: {exc}", exc_info=True)
        response = Response(
            {
                "success": False,
                "message": str(exc),
                "errors": None
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response
