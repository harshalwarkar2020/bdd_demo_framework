from behave import *


@given('Take number as {a} and {b}')
def step_impl(context, a, b):
    context.a = int(a)
    context.b = int(b)


@when('Add two numbers')
def step_impl(context):
    context.result = context.a + context.b


@then('Addition should be {c}')
def step_impl(context, c):
    assert context.result == int(c)
