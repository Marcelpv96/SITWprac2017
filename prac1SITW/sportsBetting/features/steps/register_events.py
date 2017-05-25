from behave import *


use_step_matcher('parse')


@given('Exist a event created by "{username}"')
def step_impl(context, username):
    from sportsBetting.models import Event, Team, Sport
    from django.contrib.auth.models import User

    for row in context.table:
        name = row['local'] + ' v ' + row['visitor']
        if not Event.objects.filter(name=name).exists():
            e = Event()
            e.name = name
            e.user = User.objects.get(username=username)
            e.team1 = Team.objects.get(name=row['local'])
            e.team2 = Team.objects.get(name=row['visitor'])
            s = Sport(name='Football')
            if not Sport.objects.filter(name=s.name):
                s.save()
            e.sport = Sport.objects.get(name='Football')
            e.save()


@when('I add a new event')
def step_impl(context):
    from sportsBetting.models import Sport
    s = Sport(name='Football')
    if not Sport.objects.filter(name=s.name):
        s.save()
    for row in context.table:
        context.browser.visit(context.get_url('/events/create/'))
        if context.browser.url == context.get_url('/events/create/'):
            form = context.browser.find_by_tag('form').first
            context.browser.fill('name', row['local'] + ' v ' + row['visitor'])

            context.browser.find_option_by_text('Football').first.click()
            context.browser.find_by_xpath(
                '//select[@id="id_team1"]//option[text()="' + row['local'] + '"]', ).first.click()
            context.browser.find_by_xpath(
                '//select[@id="id_team2"]//option[text()="' + row['visitor'] + '"]', ).first.click()

            form.find_by_id('team_submit').first.click()


@when('I want to delete the event "{event_name}"')
def step_impl(context, event_name):
    from sportsBetting.models import Event
    id = Event.objects.get(name=event_name).id
    context.browser.visit(context.get_url('/events/delete/' + str(id)))


@when('I delete the event')
def step_impl(context):
    form = context.browser.find_by_tag('form').first
    form.find_by_css('.btn').first.click()
    assert context.browser.url == context.get_url('/events/list_events/')
