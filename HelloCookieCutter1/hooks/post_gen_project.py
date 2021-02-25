print("This is run after cookiecutter is generated!")

{%- if cookiecutter.greeting_recipient == "Hsin" %}

print("Is this printed?")
print("Oh yes! Hello {{ cookiecutter.greeting_recipient}}!")

{%- endif %}