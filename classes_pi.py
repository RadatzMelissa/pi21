''' O arquivo contém duas classes: Pessoa e Animal_adocao, que estão 
    sendo utilizadas na plataforma CRUD de animais perdidos 
    ou que estão para adoção.
    
    - Grupo 9 de PI - sistema de adoção de animais
    Aluna: Melissa Radatz - 302 INFO
'''

# Importações 
from config import *

class Pessoa(db.Model):
    """ Esta classe representa um usuário do sistema.
    """
    # Atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    cidade = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    # Método para expressar a pessoa em forma de texto
    def __str__(self):
        return f'(id={self.id}), {self.nome}, '+\
               f'{self.email}, {self.telefone}, ' +\
                f'{self.cidade}, {self.bairro}, ' +\
                f'{self.senha}'
    
    # Expressão da classe no formato json
    def json(self):
        return {
            "id" : self.id,
            "nome" : self.nome,
            "email" : self.email,
            "telefone" : self.telefone,
            "cidade" : self.cidade,
            "bairro" : self.bairro,
            "senha" : self.senha
        }


class Animal_adocao(db.Model):
    """ Esta classe representa um animal para adoção 
    cadastrado do sistema. """
    # Atributos da classe Animal_adocao
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.String(254))
    telefone = db.Column(db.String(254))
    sexo = db.Column(db.String(254))
    tamanho = db.Column(db.String(254))
    especie = db.Column(db.String(254))
    foto = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    temperamento = db.Column(db.String(254))
    relacionamento = db.Column(db.String(254))
    inf_veterinario = db.Column(db.String(254))
    observacoes = db.Column(db.String(254))

    # Atributo de chave estrangeira
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    # Atributo de relacionamento, para acesso aos dados via objeto
    pessoa = db.relationship("Pessoa")

    # Método para expressar a pessoa em forma de texto
    def __str__(self): 
        return f'(id={self.id}), {self.nome}, {self.idade}, '+ \
            f'{self.telefone}, {self.sexo}, {self.tamanho}, {self.especie}, '+ \
            f'{self.foto}, {self.descricao}, {self.temperamento}, ' + \
            f'{self.inf_veterinario}, {self.observacoes}, {self.relacionamento}, '+ \
            f'{str(self.pessoa)}' # O str aciona o __str__ da classe Pessoa

    # Expressão da classe no formato json
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "idade":self.idade,
            "telefone":self.telefone,
            "sexo":self.sexo,
            "tamanho":self.tamanho,
            "especie": self.especie,
            "foto": self.foto,
            "descricao":self.descricao,
            "temperamento":self.temperamento,
            "relacionamento":self.relacionamento,
            "inf_veterinario":self.inf_veterinario,
            "observacoes":self.observacoes,
            "pessoa_id":self.pessoa_id,
            "pessoa":self.pessoa.json() 
        }


# Teste das classes
if __name__ == "__main__":
    # Apagar o arquivo, se ele já existir
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # Criar tabelas
    db.create_all()

    # Testar a classe Pessoa
    p1 = Pessoa(nome = "nome1", email = "email1", telefone = "11 1111-1111", 
                cidade = "cidade1", bairro =  "bairro1", senha = "senha1")
    p2 = Pessoa(nome = "nome2", email = "email2", telefone = "22 2222-2222", 
                cidade = "cidade2", bairro =  "bairro2", senha = "senha2")       
    
    # Persistir
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    # Imprimir as pessoas cadastradas
    todas = db.session.query(Pessoa).all()
    for p in todas:
        # Imprimir em formato de texto
        print(f"Pessoa: {p}")
        # Imprimir em formato json
        print(f"Pessoa em json: {p.json()}")
        # Separar as impressões para facilitar a vizualização
        print("---------------------------------")

    # Testar a classe Animal_adocao
    a1 = Animal_adocao(nome = "nome1", idade = "idade1", telefone = "11 1111-1111",
        sexo = "sexo1", tamanho = "tam1", especie = "esp1", foto = "https://foto1.com", 
        descricao = "desc1", temperamento = "temp1", relacionamento = "rel1", 
        inf_veterinario = "inf1", observacoes = "obs1", pessoa=p2)

    # Persistir
    db.session.add(a1)
    db.session.commit()

    # Imprimir o animal cadastrado em formato de texto
    print(f"Animal para adoção: {a1}")
    # Imprimir o animal cadastrado em formato json
    print(f"Animal para adoção em json: {a1.json()}")