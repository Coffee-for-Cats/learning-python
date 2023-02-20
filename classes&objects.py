class person:
    # é quase uma documentação!
    "isso deve aparecer como parte do __DOC__ de person"

    # isso é um comentário

    # def define funções em python, __init__ é o construtor da função, ou inicializador
    def __init__(self, age):
        self.age = age

    # isso é um atributo global de person, todos os objetos compartilham
    type = "human"

    # eu preciso receber self, por que ao chamar ana.eat() ele passa ana como argumento automaticamentea
    def eat(self, something):
        print(f"Person eats {something}")


# não funciona, tu precisa de uma age! Isso chama __init__
# ana = person()
ana = person(18)
# ana = person(age=18, ...) --- Também é valido!

if ana.type == person.type:
    print("Ana is an human!")

ana.eat("apple")
