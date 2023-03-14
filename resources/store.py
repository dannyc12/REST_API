import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from schemas import StoreSchema
from flask_jwt_extended import jwt_required

from models import StoreModel
from db import db
blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store

    @jwt_required()
    def delete(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"Message": "Store deleted."}


@blp.route("/store")  # use a new method view here because new route
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        # formerly 'return {'stores': list(stores.values())}
        return StoreModel.query.all()

    @jwt_required()
    @blp.arguments(StoreSchema)
    @blp.response(200, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, "Message: A store with that name already exists.")
        except SQLAlchemyError:
            abort(500, "Message: An error occurred creating the store.")
        return store
