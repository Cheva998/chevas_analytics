import dash
from flask import Flask
from flask.helpers import get_root_path
from flask_login import login_required

from config import BaseConfig


def create_app():
    '''
    This function takes the class object from the config.py file in the main folder to 
    setup the server configuration from object. Then it starts importing the files 
    layout and callbacks from the folders marketing_app, crop_detection_app, etc.
    It also calls the register_dashapp function to setup the page that contains the 
    information to render the dashapp 
    Finally returns the server with the necessary info to take into account the dash apps 
    '''
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    from app.marketing.layout import layout as layout_marketing
    from app.marketing.callbacks import register_callbacks as register_callbacks_marketing
    register_dashapp(server, 'Proyecto de Marketing', 'marketing', layout_marketing, register_callbacks_marketing)

    from app.dashapp2.layout import layout as layout2
    from app.dashapp2.callbacks import register_callbacks as register_callbacks2
    register_dashapp(server, 'Dashapp 2', 'example', layout2, register_callbacks2)

    register_extensions(server)
    register_blueprints(server)

    return server


def register_dashapp(app, title, base_pathname, layout, register_callbacks_fun):
    '''
    Function to register the dashapps it takes as arguments the app or server, the title of the app,
    the base_pathname, the layout and callbacks loaded from register app

    This part came with the cloned repo: "Meta tags for viewport responsiveness"
    the function integrates all the data from the dashapp into the server, then it sets the title, layout,
    register callback, and protect the dashviews
    '''
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    my_dashapp = dash.Dash(__name__,
                           server=app,
                           url_base_pathname=f'/{base_pathname}/',
                           assets_folder=get_root_path(__name__) + f'/{base_pathname}/assets/',
                           meta_tags=[meta_viewport])

    with app.app_context():
        my_dashapp.title = title
        my_dashapp.layout = layout
        register_callbacks_fun(my_dashapp)
    _protect_dashviews(my_dashapp)


def _protect_dashviews(dashapp):
    '''
    This function takes the dashapp and checks whether it has a login required from the server configuration
    It's still unclear where is the server configuration

    '''
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            dashapp.server.view_functions[view_func] = login_required(dashapp.server.view_functions[view_func])


def register_extensions(server):
    '''
    This function sets the information to connect to the database through SQLAlchemy, import the login
    functionality, and finally sets the migration information, to set up the database with all the fields
    required for the app to work
    '''
    from app.extensions import db
    from app.extensions import login
    from app.extensions import migrate

    db.init_app(server)
    login.init_app(server)
    login.login_view = 'main.login'
    migrate.init_app(server, db)


def register_blueprints(server):
    '''
    This function calls the webapp which contains the basic information for the server, routes, views, login,
    main index and the pages for this webapp to work.
    '''
    from app.webapp import server_bp

    server.register_blueprint(server_bp)