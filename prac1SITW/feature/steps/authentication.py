from behave import *

use_step_matcher("parse")


@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit('http://127.0.0.1:8000/accounts/register/')
    context.browser.fill('username', username)
    context.browser.fill('password1', password)
    context.browser.fill('password2', password)
    context.browser.find_by_value('Register').first.click()


@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit('http://127.0.0.1:8000/accounts/login/?next=/accounts/profile')
    context.browser.fill('username', 'admin')
    context.browser.fill('password', '1234')
    context.browser.find_by_value('login').first.click()
    assert context.browser.is_text_present('Estas loggejat correctament')


@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('logout')+'?next=/')
    assert context.browser.is_text_present('login')


@then('Server responds with page containing "{message}"')
def step_impl(context, message):
    assert context.browser.is_text_present(message)


@then('There is "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_present_by_xpath('//a[text()="'+link_text+'"]')


@then('There is no "{link_text}" link available')
def step_impl(context, link_text):
    assert context.browser.is_element_not_present_by_xpath('//a[text()="'+link_text+'"]')


@then("I'm redirected to the login form")
def step_impl(context):
    assert context.browser.url.startswith(context.get_url('login'))
