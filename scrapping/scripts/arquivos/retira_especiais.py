import logging
import os
import re

logging.basicConfig(filename=os.path.join(os.getcwd(), 'log.txt'), level=logging.DEBUG)

def remove_caracteres_arquivo(arquivo):
    logging.info(f'Iniciando remoção de caracteres inválidos do arquivo {arquivo}...')
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(arquivo, 'w', encoding='utf-8') as f:
        for linha in linhas:
            linha = re.sub('[^0-9a-zA-Z\n\.\t\-\_\(\)\,\:\;\=\+\*\/\<\>\?\!\@\#\$\%\&\~\^\"\'\{\}\[\]\|\`\ ]', '', linha)
            f.write(linha)

    logging.info(f'Concluída remoção de caracteres inválidos do arquivo {arquivo}.')


def remove_comentarios_arquivo(arquivo):
    logging.info(f'Iniciando remoção de comentários do arquivo {arquivo}...')
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(arquivo, 'w', encoding='utf-8') as f:
        comentario_aberto = False
        for linha in linhas:
            if '/*' in linha:
                comentario_aberto = True
                continue
            elif '*/' in linha:
                comentario_aberto = False
                continue
            elif comentario_aberto:
                continue
            elif linha.startswith('--'):
                continue
            
            f.write(linha)

    logging.info(f'Concluída remoção de comentários do arquivo {arquivo}.')

def remova_ultima_linha_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r+') as f:
        # Move o cursor para o final do arquivo
        f.seek(0, os.SEEK_END)

        # Encontra a posição do último caractere não vazio
        pos = f.tell() - 1
        while pos > 0 and f.read(1) != "\n":
            pos -= 1
            f.seek(pos, os.SEEK_SET)

        # Trunca o arquivo na posição do último caractere não vazio
        if pos > 0:
            f.seek(pos, os.SEEK_SET)
            f.truncate()
        else:
            f.seek(0, os.SEEK_SET)
            f.truncate()
            
def remove_linhas(codigo):
    regex = r"ALTER TABLE\s+TB_\w+\s+ALTER COLUMN COD_SEQ_\w+\s+SET DEFAULT\s+NEXTVAL\('\w+'::regclass\);\s+UPDATE\s+TB_\w+\s+SET\s+COD_SEQ_\w+\s+=\s+NEXTVAL\('\w+'\);\n\n"

    # remove as linhas com regex
    codigo_modificado = re.sub(regex, "", codigo)

    # retorna o código sem as linhas removidas
    return codigo_modificado

def remove_linhas_arquivo(arquivo, lista):
    logging.info(f'Iniciando remoção de linhas do arquivo {arquivo}...')
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(arquivo, 'w', encoding='utf-8') as f:
        contador_linhas = 0
        for i, linha in enumerate(linhas):
            if any(elemento in linha for elemento in lista):
                continue
            elif re.match(r'^\s*ALTER TABLE TB_.+', linha):
                if contador_linhas == 0:
                    contador_linhas += 1
                    continue
                elif contador_linhas < 4:
                    contador_linhas += 1
                    continue
                elif contador_linhas == 4:
                    contador_linhas = 0
                    continue
                else:
                    contador_linhas = 0
            else:
                f.write(linha)

def remove_conjuntos_multilinhas(arquivo):
    logging.info(f'Iniciando remoção de conjuntos de caracteres multilinhas do arquivo {arquivo}...')
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(arquivo, 'w', encoding='utf-8') as f:
        alter_table_encontrada = False
        for i, linha in enumerate(linhas):
            if alter_table_encontrada:
                if ');' in linha:
                    alter_table_encontrada = False
                continue
            elif re.match(r'^\s*ALTER TABLE TB_.+', linha):
                if ');' not in linha:
                    alter_table_encontrada = True
                continue
            
            f.write(linha)

    logging.info(f'Concluída remoção de conjuntos de caracteres multilinhas do arquivo {arquivo}.')

def adicionar_not_auto_increment(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        script = f.read()

    padrao = r'(COD_SEQ_\w+)\s+INTEGER\s+UNIQUE\s+NULL'
    substituicao = r'\g<1> INTEGER UNIQUE NOT NULL AUTO_INCREMENT'
    script = re.sub(padrao, substituicao, script)

    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(script)

    logging.info(f'Concluída remoção de linhas do arquivo {arquivo}.')

if __name__ == '__main__':
    arquivo = r'C:\Users\lucas\Documents\GitHub\Python\Anls-dados\desafios\faturamento_estados\scrapping\scripts\arquivos\script.sql'
    remove_caracteres_arquivo(arquivo)
    remove_comentarios_arquivo(arquivo)
    remove_linhas_arquivo(arquivo, ['CREATE SEQUENCE', 'DROP SEQUENCE'])
    remove_linhas_arquivo(arquivo, ['INCREMENT 1', 
                                    'MINVALUE 0', 
                                    'MAXVALUE 9999', 
                                    'START 1', 
                                    'CACHE 1', 
                                    "SET COD_SEQ_ESTADO = NEXTVAL('co_seq_estado')",
                                    "SET COD_SEQ_MUNICIPIOS = NEXTVAL('co_seq_municipio')",
                                    "SET COD_SEQ_REGIAO = NEXTVAL('co_seq_regiao')",
                                    'ALTER TABLE  TB_MUNICIPIO',
                                    'DROP TABLE TB_REGIAO;',
                                    'DROP TABLE TB_ESTADO;',
                                    'DROP TABLE TB_MUNICIPIO;',
                                    "ALTER COLUMN COD_SEQ_REGIAO",
                                    "SET DEFAULT  NEXTVAL('co_seq_regiao'::regclass);",
                                    "UPDATE       TB_REGIAO",
                                    "SET          COD_SEQ_REGIAO = NEXTVAL('co_seq_regiao');",
                                    'ALTER TABLE  TB_ESTADO',
                                    "ALTER COLUMN COD_SEQ_ESTADO",
                                    "SET DEFAULT  NEXTVAL('co_seq_estado'::regclass);",
                                    "UPDATE       TB_ESTADO",
                                    "ALTER TABLE  TB_MUNICIPIO",
                                    "ALTER COLUMN COD_SEQ_MUNICIPIOS",
                                    "SET DEFAULT  NEXTVAL('co_seq_municipio'::regclass);",
                                    "UPDATE       TB_MUNICIPIO",
                                    "ALTER TABLE    TB_ESTADO",
                                    "ADD CONSTRAINT fk_estado",
                                    "FOREIGN KEY    (COD_REGIAO)",
                                    "REFERENCES     TB_REGIAO(COD_SEQ_REGIAO);",
                                    "ALTER TABLE    TB_MUNICIPIO",
                                    "ADD CONSTRAINT fk_municipio",
                                    "FOREIGN KEY    (COD_ESTADO)",
                                    "REFERENCES     TB_ESTADO(COD_SEQ_ESTADO);",
                                    'ALTER TABLE  TB_REGIAO'])
    remove_conjuntos_multilinhas(arquivo)
    remova_ultima_linha_arquivo(arquivo)
    adicionar_not_auto_increment(arquivo)
    logging.info(f'Concluído processamento do arquivo {arquivo}.')
