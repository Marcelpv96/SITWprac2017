from behave import *

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth.models import User
    if not User.objects.filter(username=username):
        User.objects.create_user(username=username, email="email@test.com", password=password)


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url('/accounts/login/?next=/accounts/profile/'))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('login').first.click()
    assert context.browser.is_text_present('Estas loggejat correctament')


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('logout')+'?next=/')
    assert context.browser.is_text_present('Login')


@then('Server responds with page containing "{message}"')
def step_impl(context, message):
    assert context.browser.is_text_present(message)


@then("I'm redirected to the login page")
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('/accounts/login/'))
