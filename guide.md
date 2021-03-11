# Módulo 1

## PEP 8

PEP significa Python Enhancement Proposal, que é um *Style Guide* para a programação em Python, ou seja, uma diretriz para como escrever códigos nessa linguagem. Segue abaixo algumas recomendações do [PEP-8](https://www.python.org/dev/peps/pep-0008/):

* Linhas com máximo de 79 caracteres;
* Nome de variáveis e funções utilizando *snake case* (`nome_da_variavel`);
* Identação utilizando espaços e não *tabs*;
* Separar classes com duas linhas brancas, funções com uma linha branca e seções diferentes do código com uma linha em branco;
* Importar bibliotecas em linhas diferentes;
* Utilizar espaços entre operadores aritméticos e depois de vírgulas, não usar espaços extras em Strings e depois ou antes de abrir um parênteses. Dois espaços antes de um comentário.
---

## String Formatting

Para formatar uma string, basta utilizar os *placeholders* `{}` e o método `.format()`, que irá os substituir. Exemplo:

```py
nome = 'Gabriel'
idade = 20
print ("Nome: {name}, idade: {age}".format(name = nome, age = idade))
```

> Ao invés de escolher uma palavra para referenciar, como foi feito com *name* e *age*, podem ser usados os números em que as substituições aparecem no `.format()`, como `print("Nome: {0}, idade: {1}".format(nome, idade))`.

* Caso o objetivo seja apenas formatar casas decimais, pode ser usado o operador `%`:
```py
pi = 3.14159265359
print ("%.5f" % pi)
```

---

## Scopes

Traram do grau de acesso às variáveis em diferentes escopos do programa. A prioridade é sempre da variável do atual escopo, ou seja, a variável local.

Uma varíavel global é simplesmente uma declarada no fluxo principal do programa, fora de qualquer escopo. Ela pode ser utilizada em qualquer escopo interior, mas não modificada. Para que ela possa ser alterada, é necessário o uso da palavra reservada `global` no escopo interno, para permitir sua alteração.

```py
cidade = "Itajuba"

def nova_cidade(nova):
    global cidade  # Para permitir que seja alterada na linha abaixo
    cidade = nova

nova_cidade("Volta Redonda")
```

---

## Classes

A palavra chave para declarar uma classe é `class`, e deve ser declarada como uma função:

```py
class MyClass:
    ...
```

> Note que segundo o PEP-8, a classe deve utilizar *CapWords* (`NomeDaClasse`).

* Quando é criado um objeto de uma classe, ele é chamado de **instância** (`my_thing = MyClass()`).

* Funções que são declaradas dentro de classes são chamadas de **métodos**, as variáveis de **atributos** e as variáveis declaradas dentro de métodos são **atributos de instâncias** (devem utilizar o método `__init__`, que é o construtor.

* Para referenciar uma instância de um método, é usada a palavra chave `self.`, semelhante ao `this.` do C++.

* Quando uma instância for usada em um método, deve ser passado o atributo `self` para o método.

## Métodos Mágicos

São métodos já existentes no Python, como o `__init__`, e todos ele ssão precedidos e sucedidos por dois *underscores*, e, por isso, são também chamados de *dunders*.

* `__init__`: Método construtor de classes, presente sempre que se deseja criar uma nova instância. Nele são declarados os atributos de instância, ou seja, variáveis que possuem valores diferentes para cada instância declarada do objeto.

* `__new__`: Esse método é responsável por criar novas instâncias, ou seja, ele próprio chama o método `__init__`. Pode ser útil o alterar quando se deseja limitar a quantidade de instâncias criadas de uma classe, por exemplo. A palavra reservada `cls` é utilizada para se referir a própria classe, semelhante ao uso de `self`, que se refere à instância. Abaixo segue um trecho de código onde esse método é utilizado:

```py
class Sun:
    n = 0  # number of instances of this class

    def __new__(cls):
        if cls.n == 0: 
            cls.n += 1
            return object.__new__(cls)  # create new object of the class
```

* `__repr__`: Esse método retorna uma *String*, e deve ser utilizado para uma representação não ambígua da classe; uma maneira de ser fazer isso é retornar o código utilizado para instanciar um novo objeto. Exemplo:

```py
class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)

payment = Transaction("000001", 9999.999)
print (payment)
# Transaction(000001, 9999.999)
```

* `__str__`: Semelhante ao método `__repr__`, o `__str__` é chamado quando a função `print()` é utilizada, mas, nesse caso, deve retornar uma *String* altamente legível, ou seja, para o usuário.

> Quando o méotodo `__str__` estiver definido, ele será o padrão de retorno do `print`, e, para usar o `__repr__`, ele deve ser chamado diretamente.

```py
class Transaction:
    def __init__(self, number, funds, status="active"):
        self.number = number
        self.funds = funds
        self.status = status

    def __repr__(self):
        return "Transaction({}, {})".format(self.number, self.funds)

    def __str__(self):
        return "Transaction {} for {} ({})".format(self.number, self.funds, self.status)


payment = Transaction("000001", 9999.999)
print (payment)
# Transaction 000001 for 9999.999 (active)
print (repr(payment))
# Transaction(000001, 9999.999) 
```

## Herança de Classes

Herança em classes se trata de herdar características de uma classe pai para uma classe filho, para que não haja necessidade de reescrever atributos e métodos que serão reutilizados.

Para definir uma classe como filha, basta passar o nome da classe pai em sua declaração:

```py
# inheritance syntax
class ChildClass(ParentClass):
    # methods and attributes
    ...
```

> Todas as classes possuem por padrão a classe `object` como classe pai, por isso os  métodos mágicos não precisam ser sempre definidos, pois são herdados de `object`.

* A função `type()` recebe um objeto e serve para verificar seu tipo, ou seja, retorna sua classe. Funciona apenas para verificar a classe imediata do objeto, ou seja, não define uma instância da classe filha como sendo da classe pai.

* Por outro lado, a função `isinstance()` recebe dois valores, o objeto e uma classe, retornando *True* ou *False*. Nesse caso, se o objeto passado for filho da classe passada, a função retornará *True*, o que permite verificar a herança de classes.

* A função `issubclass()` recebe duas classes, e verifica se a primeira é uma subclasse da segunda, retornando *True* ou *False*.

> Toda classe é uma subclasse de si mesma, logo, `issubclass(MyClass, MyClass)`, retornará *True*.

> Essa função não recebe *String*, recebe a classe em si!

# Módulo 2

## Data Mapping

Trata-se do processo de converter dados entre a linguagem de programação que está sendo utilizada para o método de organização de seu destino, que pode ser tabela, *XML*, *JSON* etc.

## Object-Relational Mapping

Aqui, os dados a serem salvos são tratados como objetos de uma classe, e permite que métodos dessa classe sejam chamados e apliquem mudança em tempo real a esses dados armazenados, por serem objetos dessa classe.

## SQL Alchemy

Essa é a biblioteca padrão para se trabalhar com SQL em Python. Trabalhar com essa biblioteca é simples, e aqui serão abordados os processos de criar a tabela, visualizar os dados da tabela e inserir um elemento na tabela.

* Criando a tabela:

```python
engine = create_engine('sqlite:///todo.db?check_same_thread=False')  # Create file 'todo.db'

Base = declarative_base()  # Base class from with the table will inherit.


class Table(Base):  # Defining the Table
    __tablename__ = 'task'  # name
    id = Column(Integer, primary_key=True)  # first column
    task = Column(String, default='task')  # second column
    deadline = Column(Date, default=datetime.today())  # third column

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)  # Creating the table
```

* Visualizando dados da database:

> Para se trabalhar com a tabela, é necessário que se inicie uma sessão na database, tanto para visualizar tanto quanto para adicionar uma nova linha.

```python
Session = sessionmaker(bind=engine)
session = Session()  # Instancing object

tasks = session.query(Table).all()
```

* Adicionando novo dado:

> O ato de criar a sessão pode ser realizado apenas um vez, tanto para ler quanto para escrever.
> 
```python
Session = sessionmaker(bind=engine)
session = Session()  # Instancing object

task_name = input("Enter task")
new_row = Table(task=task_name,
                deadline=datetime.today().date())
session.add(new_row)  # Adding new row
session.commit()  # Commiting changes
```