from flaskapp.modules.models.user_model import Users

def test_get_user_by_email(app, user):
    queried_user = Users.get_user_by_email("test@example.com")
    assert queried_user == user

def test_in_database(app, user):
    assert user.in_database() == True
    new_user = Users(email="new@example.com")
    assert new_user.in_database() == False

# Add more 
    """
        test_in_database_returns_true_for_existing_user
        test_in_database_returns_false_for_nonexistent_user
        test_register_user
        test_authenticate
        test_add_item_to_user_cart
        test_get_user_cart
        test_get_email
        test_get_id
    """