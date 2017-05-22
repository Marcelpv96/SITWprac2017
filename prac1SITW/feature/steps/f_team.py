from behave import *

use_step_matcher("parse")


@when('I list teams')
def step_impl(context):
    context.browser.visit(context.get_url('teams:list_teams'))


@when('I add a new team')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('teams:create'))
        if context.browser.url == context.get_url('teams:create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()


@when('I list teams filtered by "{search}"')
def step_impl(context, search):
    context.browser.visit(context.get_url('teams:list_teams:' + search))


@then('I found the team named "{name}"')
def step_impl(context, name):
    teams_rows = [x.text for x in context.browser.find_by_tag('td')]
    assert name in teams_rows
