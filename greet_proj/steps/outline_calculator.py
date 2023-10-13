from behave import *


@given('open calculator')
def step_impl(context):
    pass


@when('perform addition on {a} and {b}')
def step_impl(context, a, b):
    context.result = int(a) + int(b)


@then('sum should be {c}')
def step_impl(context, c):
    assert context.result == int(c)
