from behave import *
use_step_matcher("parse")


@given('Exists a team created by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from sportsBetting.models import Team
    for row in context.table:
        team = Team(created_by=user)
        for heading in row.headings:
            setattr(team, heading, row[heading])

        if not Team.objects.filter(name=team.name).exists():
            team.save()


@when('I add a new team')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/teams/create/'))
        if context.browser.url == context.get_url('/teams/create/'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(str(heading), str(row[heading]))

            form.find_by_id('team_submit').first.click()


@when('I want to edit the team "{team_name}"')
def step_impl(context, team_name):
    from sportsBetting.models import Team
    id = Team.objects.get(name=team_name).id
    context.browser.visit(context.get_url('/teams/edit/' + str(id)))


@when('I edit the team')
def step_impl(context):
    for row in context.table:
        if context.browser.url.startswith(context.get_url('/teams/edit/')):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(str(heading), str(row[heading]))

            form.find_by_id('team_submit').first.click()

    assert context.browser.url == context.get_url('/teams/list_teams/')

