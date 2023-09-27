from django import template

register = template.Library()


@register.filter(name='age')
def age_filter(age):
    month = age.days // 30
    day = age.days
    hour = (age.seconds // 60) // 60

    if month > 1:
        return f'{month} month and {day} day remain'
    else:
        if day > 0:
            return f'{day} day remain'
        elif day < 0:
            return f'{day} day ago'

        else:
            if hour >= 1:
                return f'{hour} hours remain'
            else:
                return 'some time ago membership finished'
