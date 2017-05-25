from behave import *

use_step_matcher('parse')


@when('I list bets')
def step_impl(context):
    context.browser.visit(context.get_url('/bets/list_bets'))


@then('I\'m viewing a bet list containing')
def step_impl(context):
    bets = context.browser.find_by_tag('h3')
    for i, row in enumerate(context.table):
        assert row['name'] == bets[i].text


@then('I find a bet with quota "{quota}"')
def step_impl(context, quota):
    quotas = [x.text for x in context.browser.find_by_tag('h3')]
    assert quota in quotas


@then('I find a bet with description "{description}"')
def step_impl(context, description):
    from sportsBetting.models import Bet
    u = [x.description for x in Bet.objects.all()]
    descriptions = [x.text for x in context.browser.find_by_tag('p')]
    assert description in descriptions
