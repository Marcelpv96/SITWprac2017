from behave import *
use_step_matcher('parse')


@when('I list competitions filtered by "{search}"')
def step_impl(context, search):
    url = context.get_url('/competitions/list_competitions/?search_box=' + search)
    context.browser.visit(url)


@when('I click to competition "{competition}"')
def step_impl(context, competition):
    context.browser.visit(context.get_url('/teams/list_teams/?search_box=competition:' + competition))


@then('I found the competition named "{name}"')
def step_impl(context, name):
    competitions_rows = [x.text for x in context.browser.find_by_tag('td')]
    assert name in competitions_rows
