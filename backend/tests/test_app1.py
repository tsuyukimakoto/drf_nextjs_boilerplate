from app1.apps import App1Config


# Create your tests here.
def test_app_name():
    assert App1Config.name == "app1"
