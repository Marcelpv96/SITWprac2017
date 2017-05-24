from behave import *

use_step_matcher('parse')


@when('I list events')
def step_impl(context):
    context.browser.visit(context.get_url('/events/list_teams'))


@then('I\'m viewing a event list containing')
def step_impl(context):
    events = context.browser.find_by_tag('h3')
    for i, row in enumerate(context.table):
        assert row['name'] == events[i].text

