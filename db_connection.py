import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class DbConnection:
    """
    This class is a Context-Manager - responsible to create the connection to firebase
    """
    def __init__(self):
        cred = credentials.Certificate('key.json')
        try:
            firebase_admin.get_app()  # The app was already initialized
        except ValueError:
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass
