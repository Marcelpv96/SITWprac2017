from behave import *

use_step_matcher('parse')


@when('I list events')
def step_impl(context):
    context.browser.visit(context.get_url('/events/list_events'))


@when('I list "{team}" events')
def step_impl(context, team):
    from sportsBetting.models import Team
    id = Team.objects.get(name=team).id
    context.browser.visit(context.get_url('/events/list_events/' + str(id)))


@then('I find a event named "{event_name}"')
def step_impl(context, event_name):
    events = [x.text for x in context.browser.find_by_tag('h3')]
    assert event_name in events


@then('I\'m viewing a event list containing')
def step_impl(context):
    from sportsBetting.models import Event
    u = [x.name for x in Event.objects.all()]
    events = context.browser.find_by_tag('h3')
    for i, row in enumerate(context.table):
        assert row['local'] + ' v ' + row['visitor'] == events[i].text
