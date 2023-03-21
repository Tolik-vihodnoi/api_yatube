from rest_framework import exceptions


def check_not_nonrequired_fields_or_raise_exception(serializer):
    """Проверяет наличие лишних ключей, передаваемых в теле запроса."""
    nr_fields: set = (set(serializer.__class__.Meta.read_only_fields)
                      & set(serializer.initial_data))
    if nr_fields:
        raise exceptions.PermissionDenied(
            f'Вы передаёте лишние данные! Эти поля не нужны: {nr_fields}'
        )
