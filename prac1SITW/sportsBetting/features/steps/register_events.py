from behave import *

use_step_matcher('parse')


@given('Exist a event created by "{username}"')
def step_impl(context, username):
    # TODO: Add new event to database
    pass


@when('I add a new event')
def step_impl(context):
    # TODO: Fill event form and submit
    pass


@when('I want to edit the event "{event_name}"')
def step_impl(context, event_name):
    from sportsBetting.models import Event
    id = Event.objects.get(name=event_name).id
    # TODO: Browser visits edit page for events


@when('I edit the event')
def step_impl(context):
    # TODO: Fill event form and submit
    pass



