class YesNoService:
    def ask(self, question: str) -> bool:
        valid = {"yes": True, "y": True, "si": True, "no": False, "n": False}

        while True:
            answer = input(f"{question} (y/n): " ).strip().lower()

            if answer in valid:
                return valid[answer]

            print("Intente nuevamente, valor no valido")