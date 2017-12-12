from behave import *
import time
import calc

@given(u'a test is written')
def step_impl(context):
    pass

@then(u'lets parse these single digit numbers')
def step_impl(context):
    i = 0
    for row in context.table:
        assert(calc.evaluate_single_digit(row['number']) == i)
        i = i + 1

@then(u'lets parse these positive whole numbers')
def step_impl(context):
    assert(calc.evaluate_positive_number((context.table[0])['number']) == 1)
    assert(calc.evaluate_positive_number((context.table[1])['number']) == 100)
    assert(calc.evaluate_positive_number((context.table[2])['number']) == 100000)
    assert(calc.evaluate_positive_number((context.table[3])['number']) == 124809214)
    assert(calc.evaluate_positive_number((context.table[4])['number']) == 821944014122)
    assert(calc.evaluate_positive_number((context.table[5])['number']) == 5395783105175091)
    assert(calc.evaluate_positive_number((context.table[6])['number']) == 9223372036854775807)

@then(u'lets parse these positive floating point numbers')
def step_impl(context):
    assert(calc.evaluate_floating_point_number((context.table[0])['number']) == 1)
    assert(calc.evaluate_floating_point_number((context.table[1])['number']) == 1.01)
    assert(calc.evaluate_floating_point_number((context.table[2])['number']) == 1.0123)
    assert(calc.evaluate_floating_point_number((context.table[3])['number']) == 213.124)
    assert(calc.evaluate_floating_point_number((context.table[4])['number']) == 53215.21124)

@then(u'lets parse these positive single digit hexadecimal numbers')
def step_impl(context):
    i = 0
    for row in context.table:
        assert(calc.evaluate_single_hexadecimal_digit(row['number']) == i)
        i = i + 1

@then(u'lets parse all combinations of positive hexadecimal numbers')
def step_impl(context):
    for row in context.table:
        for row2 in context.table:
            assert(calc.evaluate_hexadecimal(row['number'] + row2['number']) == (calc.evaluate_single_hexadecimal_digit(row['number']) * 16 + calc.evaluate_single_hexadecimal_digit(row2['number'])))

@then(u'lets evaluate the entire system')
def step_impl(context):
    assert(calc.evaluate_section((context.table[0])['number']) == -10000)
    assert(calc.evaluate_section((context.table[1])['number']) == -124809214)
    assert(calc.evaluate_section((context.table[2])['number']) == -821944014122)

    assert(calc.evaluate_section((context.table[3])['number']) == -1.0123)
    assert(calc.evaluate_section((context.table[4])['number']) == -213.124)
    assert(calc.evaluate_section((context.table[5])['number']) == -53215.21124)

    assert(calc.evaluate_section((context.table[6])['number']) == 1)
    assert(calc.evaluate_section((context.table[7])['number']) == 10)
    assert(calc.evaluate_section((context.table[8])['number']) == 175)
    assert(calc.evaluate_section((context.table[9])['number']) == 196)
    assert(calc.evaluate_section((context.table[10])['number']) == 249)
