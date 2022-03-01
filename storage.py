from db_connection import DbConnection


class Storage:
    @staticmethod
    def set(collection, data):
        with DbConnection() as db:
            try:
                doc_ref = db.collection(collection).document()
                doc_ref.set(data)
            except Exception as e:
                raise Exception(str(e))

    @staticmethod
    def get(collection):
        with DbConnection() as db:
            try:
                return list(x.to_dict() for x in db.collection(collection).stream())
            except Exception as e:
                raise Exception(str(e))
