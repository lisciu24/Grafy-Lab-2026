from dataclasses import dataclass
from typing import Any

@dataclass
class Field:
    key: str
    label: str
    type: str
    default: Any = None
    required: bool = True
    options: list[Option] | None = None
    item_type: str = "str"

@dataclass
class Option:
    key: str
    label: str
    fields: list[Field] | None = None

_converters = {
    "str": str,
    "int": int,
    "float": float
}

def _check_raw(field: Field, raw: Any):
    if field.default is not None:
        print(f"Użyto wartości domyślnej: {field.default}")
        return True, field.default

    if not field.required:
        print("Pominięto")
        return True, None
    else:
        print("Wartość wymagana")

    return False, None

def _read_list(field: Field) -> list[str|int|float] | None:
    assert field.item_type in _converters, "Niepoprawny typ dla wartości listy"
    assert field.default is None or type(field.default) == list[_converters[field.item_type]], "Default value must be a list of item_type values"
    
    conv = _converters[field.item_type]
    while True:
        suffix = f" [{field.default}]" if field.default is not None else ""
        raw = input(f"{field.label}{suffix} (oddziel spacjami): ").strip()

        if not raw:
            ret, val = _check_raw(field, raw)
            if ret: return val

            continue

        try:
            return [conv(x) for x in raw.split()]
        except ValueError:
            print(f"Błąd podczas wprowadzania danych, oczekiwano listy typu: {field.item_type}")


def _read_value(field: Field) -> str | int | float | None:
    assert field.default is None or type(field.default) == _converters[field.type], "Default value must match field type"

    while True:
        suffix = f" [{field.default}]" if field.default is not None else ""
        raw = input(f"{field.label}{suffix}: ").strip()

        if not raw:
            ret, val = _check_raw(field, raw)
            if ret: return val

            continue

        try:
            return _converters[field.type](raw)
        except ValueError as error:
            print(f"Niepoprawna warość: {error}")
            
def _read_choice(field: Field) -> Option | None:
    assert field.options, "Specify options for choice type"
    assert field.default is None or type(field.default) == Option, "Default may be None or Option for choice type"

    suffix = f" [{field.default.label}]" if field.default is not None else ""
    print(f"\n{field.label}{suffix}")
    for i, option in enumerate(field.options, 1):
        print(f" ({i}) {option.label}")

    while True:
        raw = input("Wybór: ").strip()

        if not raw:
            ret, val = _check_raw(field, raw)
            if ret: return val

            continue

        try:
            choice = int(raw)
            if 1 <= choice <= len(field.options):
                return field.options[choice -1]
            else:
                raise ValueError

        except ValueError:
            print("Podaj numer opcji")

def get_input(config: list[Field]) -> dict[str, Any]: 
    result = {}

    for field in config:
        if field.type == "choice":
            selected = _read_choice(field)
            if selected:
                if selected.fields: 
                    result[field.key] = {selected.key: get_input(selected.fields)}
                else:
                    result[field.key] = selected.key 
            else:
                result[field.key] = None
        elif field.type == "list":
            result[field.key] = _read_list(field)
        elif field.type in _converters:
            result[field.key] = _read_value(field)
        else:
            print(f"Nieobsługiwany typ: {field.type} dla {field}")

    return result