import talisker
import flask
from flask import Blueprint, request, session, make_response, current_app as app

from canonicalwebteam.store_base.packages.logic import get_packages, get_snaps_account_info
from canonicalwebteam.store_base.utils.config import PACKAGE_PARAMS

from canonicalwebteam.store_base.auth.authentication import login_required

package = Blueprint(
    "store",
    __name__,
)


@package.route("/store")
def store():
    app_name = app.name
    params = PACKAGE_PARAMS[app_name]
    store, fields, size = params["store"], params["fields"], params["size"]
    page = int(request.args.get("page", 1))
    return get_packages(store, fields, size, page)

@package.route("/<package_type>")
@login_required
def package_type(package_type):
    app_name = app.name
    publisher = PACKAGE_PARAMS[app_name]["publisher"]
    
    publisher_api = publisher(talisker.requests.get_session())
    # this endpoint needs to be made generic in the future, so we wont have to check for package_type
    if package_type == "charms" or "bundles":
        publisher_packages = publisher_api.get_account_packages(
            session["account-auth"], "charm", include_collaborations=True
        )
        page_type = request.path[1:1]

        response = make_response({
            "published_packages": [
                package
                for package in publisher_packages
                if package["status"] == "published" and package["type"] == page_type
            ],
            "registered_packages": [
                package
                for package in publisher_packages
                if package["status"] == "registered" and package["type"] == page_type
            ],
            "page_type": page_type,
        })
        return response

    if package_type == "snaps":
        account_info = publisher_api.get_account(flask.session)

        user_snaps, registered_snaps = get_snaps_account_info(account_info)
        flask_user = flask.session["publisher"]

        response = make_response({
            "snaps": user_snaps,
            "current_user": flask_user["nickname"],
            "registered_snaps": registered_snaps,
        })

        return response
