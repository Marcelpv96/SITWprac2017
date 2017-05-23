from behave import *
use_step_matcher("parse")


@given('Exist a competition created by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    from sportsBetting.models import Competition, Team

    for row in context.table:
        name = row['name']
        if not Competition.objects.filter(name=name):
            short_name = row['short_name']
            teams_name = row['teams'].split(',')
            c = Competition()
            c.name = name
            c.short_name = short_name
            c.user = User.objects.get(username=username)
            c.save()
            for n in teams_name:
                c.teams.add(Team.objects.get(name=n))


@when('I add a new competition')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('/competitions/create/'))
        form = context.browser.find_by_tag('form').first
        name = row['name']
        short_name = row['short_name']
        teams_name = row['teams'].split(',')

        context.browser.fill('name', name)
        context.browser.fill('short_name', short_name)
        for n in teams_name:
            context.browser.find_option_by_text(n).first.click()

        form.find_by_id('team_submit').first.click()

