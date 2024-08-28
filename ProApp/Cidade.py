from Banco import Banco

class Cidade(object):
    def __init__(self, cidade_id, nome: str, uf:str):
        self.dict: {}

        self.id = cidade_id
        self.name = nome
        self.uf = uf

    def insert(self) -> str:
        try:
            Banco.cursor.execute("insert into city (name, uf) values ('" + self.name + "', '" + self.uf + "'")
            Banco.commit()
            Banco.cursor.close()

            return "Cidade cadastrada com sucesso!"

        except:
            return "Erro ao cadastrar cidade!"

    def update(self) -> str:
        try:
            Banco.cursor.execute("update city set name = '" + self.nome + "', '" + self.uf + "'")
            Banco.commit()
            Banco.cursor.close()

            return "Cidade atualizada com sucesso!"

        except:
            return "Erro ao atualizar cidade!"

    def delete(self) -> str:
        try:
            Banco.cursor.execute("delete from city where id = '" + self.id + "'")
            Banco.commit()
            Banco.cursor.close()

            return "Cidade excluida com sucesso!"
        except:
            return "Erro ao excluir cidade!"

    def select(self, cidade_id) -> str:
        try:
            Banco.cursor.execute("select * from city where id = '" + cidade_id +"'")
            Banco.commit()
            Banco.cursor.close()

            data = []

            for row in data:
                self.id = row[0]
                self.nome = row[1]
                self.uf = row[2]

            return "Busca feita com sucesso!"

        except:
            return "Erro ao buscar cidade!"