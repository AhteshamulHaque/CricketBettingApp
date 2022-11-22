from flask import Blueprint

scheduler_bp = Blueprint("scheduler", __name__)

@scheduler_bp.route("/")
def scheduler_status():
    return "status of scheduler"

@tree_mold.route("/start")
def roots():
    return "And roots as well"

@tree_mold.route("/rings")
@tree_mold.route("/rings/&lt;int:year&gt;")
def rings(year=None):
    return "Looking at the rings for {year}".format(year=year)


from tree_workshop import tree_mold

app.register_blueprint(tree_mold, url_prefix="/oak")
app.register_blueprint(tree_mold, url_prefix="/fir")
app.register_blueprint(tree_mold, url_prefix="/ash")


