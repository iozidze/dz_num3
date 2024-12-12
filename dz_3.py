# import argparse
import toml
import re
import sys
import argparse

class ConfigTransformer:
    def __init__(self):
        self.constants = {}

    def validate_name(self, name):
        """Проверяет, соответствует ли имя синтаксическим требованиям."""
        if not re.match(r"^[_a-zA-Z]+$", name):
            raise ValueError(f"Invalid name '{name}'.")

    def transform_value(self, value):
        """Трансформирует значение из TOML в учебный язык."""
        if isinstance(value, int):  # Число
            return str(value)
        elif isinstance(value, dict):  # Словарь
            items = ",\n ".join(f"{k} : {self.transform_value(v)}" for k, v in value.items())
            return f"$[\n {items}\n]"
        else:
            raise ValueError(f"Unsupported value type: {type(value)}")

    def transform(self, data):
        """Преобразует TOML-данные в выходной формат."""
        lines = []
        for key, value in data.items():
            self.validate_name(key)
            if key.startswith("def "):  # Объявление константы
                const_name = key.split(" ")[1]
                self.validate_name(const_name)
                self.constants[const_name] = self.transform_value(value)
                lines.append(f"def {const_name} = {self.constants[const_name]}")
            elif key.startswith("|"):  # Вычисление константы
                const_name = key[1:-1]
                self.validate_name(const_name)
                if const_name not in self.constants:
                    raise ValueError(f"Undefined constant '{const_name}'.")
                lines.append(f"|{const_name}|")
            else:  # Обычная запись
                lines.append(f"{key} = {self.transform_value(value)}")
        return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Transform TOML to custom configuration language.")
    parser.add_argument("input_file", help="Path to the input TOML file.")
    args = parser.parse_args()

    try:
        # Чтение строк из файла
        with open(args.input_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Парсинг TOML
        toml_data = toml.loads(content)

        # Преобразование
        transformer = ConfigTransformer()
        output = transformer.transform(toml_data)

        # Вывод результата
        print(output)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
