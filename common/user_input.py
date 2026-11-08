from dataclasses import dataclass
from typing import Any

@dataclass
class Field:
    key: str
    label: str
    type: str
    default: Any = None
    options: list[Option] | None = None

@dataclass
class Option:
    key: str
    label: str
    fields: list[Field] | None = None

def _read_value(field: Field) -> str | int | float:
    while True:
        suffix = f" [{field.default}]" if field.default is not None else ""
        raw = input(f"{field.label}{suffix}: ").strip()

        if not raw:
            if field.default is not None:
                return field.default
            continue

        try:
            if field.type == "str":
                return raw
            if field.type == "int":
                return int(raw)
            if field.type == "float":
                return float(raw)
            else:
                raise ValueError(f"Nieobsługiwany typ: {field.type}")
        except ValueError as error:
            print(f"Niepoprawna warość: {error}")
            
def _read_choice(field: Field) -> Option:
    assert(field.options is not None)

    print(f"\n{field.label}")
    for i, option in enumerate(field.options, 1):
        print(f" ({i}) {option.label}")

    while True:
        try:
            choice = int(input("Wybór: "))
            if 1 <= choice <= len(field.options):
                return field.options[choice -1]

        except ValueError:
            print("Podaj numer opcji")

def get_input(config: list[Field]) -> dict[str, Any]: 
    result = {}

    for field in config:
        if field.type == "choice":
            selected = _read_choice(field)
            if selected.fields: 
                result[field.key] = {selected.key: get_input(selected.fields)}
            else:
                result[field.key] = selected.key
        else:
            result[field.key] = _read_value(field)

    return result