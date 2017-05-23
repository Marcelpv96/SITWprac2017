from behave import *
use_step_matcher("parse")

@when('I list teams')
def step_impl(context):
    context.browser.visit('http://127.0.0.1:8000/teams/list_teams')


@when('I list teams filtered by "{search}"')
def step_impl(context, search):
    url = context.get_url('/teams/list_teams/?search_box=' + search)
    context.browser.visit(url)


@when('I add a new team')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/teams/create/'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(str(heading), str(row[heading]))

        form.find_by_id('team_submit').first.click()


@then('I found the team named "{name}"')
def step_impl(context, name):
    teams_rows = [x.text for x in context.browser.find_by_tag('td')]
    assert name in teams_rows


@given('Exists a team created by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    u = [x.username for x in User.objects.all()]
    user = User.objects.get(username=username)
    from sportsBetting.models import Team
    for row in context.table:
        team = Team(created_by=user)
        for heading in row.headings:
            setattr(team, heading, row[heading])

        team.save()



@when('I edit the team "{team_name}"')
def step_impl(context, team_name):
    from sportsBetting.models import Team
    id = Team.objects.get(name=team_name).id
    context.browser.visit(context.get_url('/teams/edit/' + str(id)))