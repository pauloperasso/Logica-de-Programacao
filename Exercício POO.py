class Funcionario:
    def __init__(self, nome, salario, senha_acesso):
        self.nome = nome
        self._salario = salario if salario >= 1000 else 1000
        self.__senha_acesso = senha_acesso

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor >= 1000:
            self._salario += valor
        else:
            print("Salário não pode ser menor que 1.000.")

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self._salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, senha_acesso, departamento):
        super().__init__(nome, salario, senha_acesso)
        self.departamento = departamento

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Departamento: {self.departamento}")

        try:
            print(f"Senha de acesso: {self.__senha_acesso}")
        except AttributeError:
            print("Não é possível acessar __senha_acesso diretamente (privado).")

# Código principal
if __name__ == "__main__":
    f = Funcionario("João", 1200, "abc123")
    g = Gerente("Maria", 2000, "xyz789", "TI")

    print("\n--- Dados do Funcionário ---")
    f.mostrar_dados()

    print("\n--- Dados do Gerente ---")
    g.mostrar_dados()

    print("\nTentando alterar salário para valor inválido (500):")
    f.salario = 500  # Não deve permitir

    print("\nAcessando atributos:")
    print(f"Nome (público): {f.nome}")
    print(f"Salário (protegido): {f._salario}")
    try:
        print(f"Senha de acesso (privado): {f.__senha_acesso}")
    except AttributeError:
        print("Não é possível acessar __senha_acesso diretamente (privado).")