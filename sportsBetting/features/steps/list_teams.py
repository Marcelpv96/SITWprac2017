from behave import *
use_step_matcher("parse")


@when('I list teams filtered by "{search}"')
def step_impl(context, search):
    url = context.get_url('/teams/list_teams/?search_box=' + search)
    context.browser.visit(url)


@when('I list teams')
def step_impl(context):
    context.browser.visit(context.get_url('/teams/list_teams'))


@then('I\'m viewing a team list containing')
def step_impl(context):
    teams = context.browser.find_by_tag('h3')
    for i, row in enumerate(context.table):
        assert row['name'] == teams[i].text


@then('I found the team named "{name}"')
def step_impl(context, name):
    teams_rows = [x.text for x in context.browser.find_by_tag('h3')]
    assert name in teams_rows
