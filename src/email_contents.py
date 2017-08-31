contents = {
    {% for interest in interests %}
        '{{ interest.name }}': '''{{ interest.text }}''',
    {% endfor %}
}
