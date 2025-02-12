import logging

class RequestContextFilter(logging.Filter):
    def filter(self, record):
        # Add custom context, e.g., request ID, user ID
        from asgiref.local import Local
        context = Local()  # Thread-safe, request-safe
        record.request_id = getattr(context, 'request_id', 'N/A')
        record.user_id = getattr(context, 'user_id', 'N/A')
        return True
