import re

#O script é muito antigo, então vamos fazer uma reestruturação para atualizar para a versão atual do postgresql.
# Leitura do arquivo com o código a ser modificado
with open(r'scrapping\scripts\arquivos\script.sql', 'r', encoding='utf-8') as f:
    sql_code = f.read()

# Expressão regular para substituir as sequências
sql_code = re.sub(r'CREATE SEQUENCE (\w+)\s+INCREMENT\s+\d+\s+MINVALUE\s+0\s+MAXVALUE\s+9999\s+START\s+1\s+CACHE\s+1;',
                  r'CREATE SEQUENCE \1 START 1;',
                  sql_code)

# Expressão regular para substituir o tipo de dados do campo BANDEIRA
sql_code = re.sub(r'--\s*BANDEIRA\s+OID\s+NOT\s+NULL,', '', sql_code)

# Expressão regular para substituir as constraints de relacionamento
sql_code = re.sub(r'ALTER TABLE\s+(\w+)\s+ADD\s+CONSTRAINT\s+(\w+)\s+FOREIGN\s+KEY\s+\((\w+)\)\s+REFERENCES\s+(\w+)\((\w+)\);',
                  r'ALTER TABLE \1 ADD CONSTRAINT \2 FOREIGN KEY (\3) REFERENCES \4(\5) ON DELETE CASCADE ON UPDATE CASCADE;',
                  sql_code)

# Escrita do código modificado em outro arquivo
with open(r'scrapping\scripts\arquivos\script_modificado.sql', 'w') as f:
    f.write(sql_code)
'''
A substituição das sequências é feita pela primeira expressão regular, 
que encontra a declaração de criação de sequência e altera os parâmetros 
para a sintaxe do PostgreSQL. A segunda expressão regular remove a declaração do campo BANDEIRA, 
que não é suportado pelo PostgreSQL. A terceira expressão regular substitui as constraints de relacionamento, 
adicionando as cláusulas ON DELETE CASCADE e ON UPDATE CASCADE para garantir que as operações de exclusão 
e atualização sejam propagadas para as tabelas relacionadas.

O código modificado é então gravado em um novo arquivo chamado código_modificado.sql. 
É importante ressaltar que, dependendo da complexidade do código original, pode ser necessário ajustar 
as expressões regulares para obter a substituição correta.
'''

