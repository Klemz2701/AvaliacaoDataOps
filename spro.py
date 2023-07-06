import pandas as pd
from pymongo import MongoClient

conexao = MongoClient("mongodb://localhost:27017/")
db = conexao["spro"]
collection_carros = db["Carros"]
collection_montadoras = db["Montadoras"]

data_carros = [["Onix", "Prata", "Chevrolet"],
               ["Polo", "Branco", "Volkswagen"],
               ["Sandero", "Prata", "Renault"],
               ["Fiesta", "Vermelho", "Ford"],
               ["City", "Preto", "Honda"]]

data_montadora = [["Chevrolet", "EUA"],
                  ["Volkswagen", "Alemanha"],
                  ["Renault", "França"],
                  ["Ford", "EUA"],
                  ["Honda", "Japão"]]

df_carros = pd.DataFrame(data_carros, columns=["Carro", "Cor", "Montadora"])

df_montadoras = pd.DataFrame(data_montadora, columns=["Montadora", "País"])

x = collection_carros.insert_many(df_carros.to_dict('records'))

y = collection_montadoras.insert_many(df_montadoras.to_dict('records'))