import pandas as pd

atividades_complementares = [

    # Categoria 1 - Extensão
    {"tipo_atividade": "Participação na organização de eventos de extensão",
     "comprovacao_necessaria": "Comprovante de participação.",
     "horas_maximas": 100, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Participação em grupos de competição acadêmica da UFBA",
     "comprovacao_necessaria": "Certificado ou declaração de participação com registro de data.",
     "horas_maximas": 150, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Atividades em empresas juniores da UFBA",
     "comprovacao_necessaria": "Relatório do professor responsável.",
     "horas_maximas": 100, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Estágio supervisionado",
     "comprovacao_necessaria": "Plano de estágio e relatório de conclusão.",
     "horas_maximas": 90, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Participação em projetos de extensão",
     "comprovacao_necessaria": "Certificado ou declaração com carga mínima de 50 horas.",
     "horas_maximas": 100, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Participação em evento de extensão",
     "comprovacao_necessaria": "Comprovante de apresentação ou cópia da publicação.",
     "horas_maximas": 60, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Trabalho científico apresentado em evento de extensão",
     "comprovacao_necessaria": "Certificado de participação com registro de data.",
     "horas_maximas": 90, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Premiação em trabalhos de extensão",
     "comprovacao_necessaria": "Cópia do documento de premiação.",
     "horas_maximas": 100, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Instrutor de oficina e/ou curso de extensão",
     "comprovacao_necessaria": "Relatório do professor orientador ou certificado.",
     "horas_maximas": 100, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Monitor de oficina e/ou curso de extensão",
     "comprovacao_necessaria": "Relatório do professor orientador ou certificado.",
     "horas_maximas": 90, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Atividade curricular em comunidade e sociedade (ACCS) ou disciplinas com CH de extensão",
     "comprovacao_necessaria": "Comprovação de aprovação na disciplina.",
     "horas_maximas": 120, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Participação em atividades administrativas/organizacionais do Colegiado ou Instituto de Computação",
     "comprovacao_necessaria": "Relatório do professor responsável.",
     "horas_maximas": 100, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Atividades de Extensão em outras IES",
     "comprovacao_necessaria": "Certificado emitido pela outra IES.",
     "horas_maximas": 60, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Visitas técnicas monitoradas por docente da Instituição",
     "comprovacao_necessaria": "Certificado ou declaração com data.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "1"},

    {"tipo_atividade": "Participação em olimpíadas e/ou maratonas na área de computação",
     "comprovacao_necessaria": "Certificado ou declaração de participação.",
     "horas_maximas": 60, "horas_feitas": 0, "categoria": "1"},

    # Categoria 2a - Ensino
    {"tipo_atividade": "Atividade Institucional de Monitoria",
     "comprovacao_necessaria": "Certificado com registro de data e carga mínima de 20h.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2a"},

    {"tipo_atividade": "Programa ou Grupo de Educação Tutorial",
     "comprovacao_necessaria": "Certificado com registro de data e carga mínima de 20h.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2a"},

    {"tipo_atividade": "Grupo de Estudo sob orientação de docente da UFBA",
     "comprovacao_necessaria": "Certificado com registro de data e carga mínima de 20h.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2a"},

    # Categoria 2b - Pesquisa
    {"tipo_atividade": "Participação em projetos de iniciação científica",
     "comprovacao_necessaria": "Certificado com registro de data e carga mínima de 20h.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2b"},

    {"tipo_atividade": "Apresentação de trabalhos (oral ou pôster) em eventos científicos",
     "comprovacao_necessaria": "Comprovante de apresentação.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2b"},

    {"tipo_atividade": "Trabalho publicado em periódico com comitê científico",
     "comprovacao_necessaria": "Publicação do artigo.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2b"},

    {"tipo_atividade": "Trabalho publicado em anais de conferência nacional/internacional",
     "comprovacao_necessaria": "Publicação do artigo.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2b"},

    {"tipo_atividade": "Trabalho publicado em anais de conferência regional",
     "comprovacao_necessaria": "Publicação do artigo.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2b"},

    {"tipo_atividade": "Premiação em trabalhos de pesquisa",
     "comprovacao_necessaria": "Cópia do documento de premiação.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2b"},

    # Categoria 2c - Vivência Profissional
    {"tipo_atividade": "Atividades de Gestão de Redes de Computadores Acadêmicas",
     "comprovacao_necessaria": "Relatório de professor responsável.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2c"},

    {"tipo_atividade": "Certificação na área de tecnologia",
     "comprovacao_necessaria": "Certificado emitido por Instituição reconhecida.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2c"},

    {"tipo_atividade": "Treinamento profissional na área de formação",
     "comprovacao_necessaria": "Certificado ou declaração com conteúdo, data e CH.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2c"},

    # Categoria 2d - Eventos Técnicos Científicos
    {"tipo_atividade": "Participação em eventos técnicos científicos",
     "comprovacao_necessaria": "Certificado ou declaração de participação com data.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2d"},

    {"tipo_atividade": "Associação em sociedade científica",
     "comprovacao_necessaria": "Carteira de sócio ou declaração.",
     "horas_maximas": 10, "horas_feitas": 0, "categoria": "2d"},

    {"tipo_atividade": "Premiação em olimpíadas/maratonas na área de computação",
     "comprovacao_necessaria": "Certificado ou declaração de premiação.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2d"},

    # Categoria 2e - Intervenção Organizacional
    {"tipo_atividade": "Participação em comissão organizadora de eventos",
     "comprovacao_necessaria": "Certificado ou declaração com data.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2e"},

    {"tipo_atividade": "Participação em eventos como ministrante de cursos",
     "comprovacao_necessaria": "Certificado ou declaração com data.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2e"},

    {"tipo_atividade": "Coordenação de congressos, simpósios e semanas científicas",
     "comprovacao_necessaria": "Certificado ou declaração com data.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2e"},

    {"tipo_atividade": "Desenvolvimento de solução tecnológica",
     "comprovacao_necessaria": "Certificado ou declaração de registro/autoria.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2e"},

    # Categoria 2f - Representação Estudantil
    {"tipo_atividade": "Mandato de representação discente na UFBA",
     "comprovacao_necessaria": "Ata de Posse e declaração.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2f"},

    {"tipo_atividade": "Representação discente em Unidades de Ensino",
     "comprovacao_necessaria": "Ata de Eleição e declaração.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2f"},

    {"tipo_atividade": "Representação estudantil em sociedades científicas",
     "comprovacao_necessaria": "Certificado ou declaração da sociedade.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2f"},

    # Categoria 2g - Formação Interdisciplinar
    {"tipo_atividade": "Cursos de Idiomas (nível intermediário ou superior)",
     "comprovacao_necessaria": "Certificado com data e carga horária.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2g"},

    {"tipo_atividade": "Certificação de proficiência em língua estrangeira",
     "comprovacao_necessaria": "Certificado por instituição reconhecida.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2g"},

    {"tipo_atividade": "Disciplinas cursadas fora da matriz curricular do BCC",
     "comprovacao_necessaria": "Registro da disciplina no Histórico Escolar.",
     "horas_maximas": 30, "horas_feitas": 0, "categoria": "2g"},

    # Categoria 2h - Outros
    {"tipo_atividade": "Participação em atividades físicas (dança, esportes, etc.)",
     "comprovacao_necessaria": "Certificado ou declaração da instituição.",
     "horas_maximas": 20, "horas_feitas": 0, "categoria": "2h"},

    {"tipo_atividade": "Participação em atividades culturais",
     "comprovacao_necessaria": "Certificado ou declaração com carga mínima de 40h.",
     "horas_maximas": 20, "horas_feitas": 0, "categoria": "2h"},

    {"tipo_atividade": "Doação de sangue",
     "comprovacao_necessaria": "Atestado de Doação (máximo 2 doações).",
     "horas_maximas": 10, "horas_feitas": 0, "categoria": "2h"},
]

df = pd.DataFrame(atividades_complementares)

# Soma de horas feitas por categoria
def horas_por_categoria(df):
    return df.groupby("categoria")["horas_feitas"].sum()

# Soma de horas faltantes por atividade
def faltam_por_atividade(df):
    df["faltam"] = df["horas_maximas"] - df["horas_feitas"]
    return df[["tipo_atividade", "faltam"]]


# Ver se alguma categoria ultrapassou seu limite (com base no dicionário de limites)
def checar_limites_categoria(df, limites_categoria):
    soma_categoria = df.groupby("categoria")["horas_feitas"].sum()
    excesso = {}
    for categoria, horas_max in limites_categoria.items():
        horas = soma_categoria.get(categoria, 0)
        excesso[categoria] = max(0, horas - horas_max)
    return excesso

limites_categoria = {
    "1": 330,
    "2a": 30,
    "2b": 30,
    "2c": 30,
    "2d": 30,
    "2e": 30,
    "2f": 30,
    "2g": 30,
    "2h": 20
}


print("Horas feitas por categoria:")
print(horas_por_categoria(df))
print()

print("Horas faltantes por atividade:")
print(faltam_por_atividade(df))
print()

print("Progresso por atividade:")
print(progresso_por_atividade(df))
print()

print("Excesso de horas por categoria:")
print(checar_limites_categoria(df, limites_categoria))
