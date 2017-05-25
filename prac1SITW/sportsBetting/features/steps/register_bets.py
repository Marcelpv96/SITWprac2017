from behave import *
from django.db.models import Q

use_step_matcher('parse')


@given('Exist a bet created by "{username}"')
def step_impl(context, username):
    from sportsBetting.models import Bet
    from sportsBetting.models import Event
    from django.contrib.auth.models import User

    for row in context.table:
        event = Event.object.get(name=row['event'])
        quota = float(row['quota'])
        desc = row['description']
        user = User.objects.get(username=username)

        if not Bet.objects.filter(Q(event=event) & Q(desc=desc)).exists():
            b = Bet(event=event, quota=quota, description=desc, user=user)
            b.save()


@when('I add a bet on "{event_name}"')
def step_impl(context, event_name):
    for row in context.table:
        context.browser.visit(context.get_url('/bets/create/'))
        if context.browser.url == context.get_url('/bets/create/'):
            form = context.browser.find_by_tag('form').first
            context.browser.find_option_by_text(event_name).first.click()
            context.browser.fill('quota', row['quota'])
            context.browser.fill('description', row['description'])
            form.find_by_id('team_submit').first.click()
