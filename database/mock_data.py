"""
Dados de demonstração — espelham o esquema SQL fornecido (sys_organizacao,
comp_favorecido, fin_titulo, fin_conta_bancaria).

Quando o Supabase estiver conectado, este módulo será substituído por
queries em database/queries.py mantendo a MESMA SHAPE de retorno.
"""

# ----------------------------------------------------------------------
# sys_organizacao (filtradas por tenant_id)
# ----------------------------------------------------------------------
ORGANIZACOES = [
    {"id": "org-1", "nome": "Matriz - Rio Verde",       "tipo": "Sede",     "cidade": "Rio Verde, GO", "saldo": 1284750.42},
    {"id": "org-2", "nome": "Filial Goiânia",           "tipo": "Filial",   "cidade": "Goiânia, GO",   "saldo":  487320.15},
    {"id": "org-3", "nome": "Filial Brasília",          "tipo": "Filial",   "cidade": "Brasília, DF",  "saldo":  218990.80},
    {"id": "org-4", "nome": "Unidade de Armazenagem",   "tipo": "Unidade",  "cidade": "Jataí, GO",     "saldo":   95430.00},
]

# ----------------------------------------------------------------------
# comp_favorecido
# ----------------------------------------------------------------------
FAVORECIDOS = [
    {"id": 1, "nome": "Indústria Brasileira de Insumos S.A.", "tipo": "pessoa_juridica", "doc": "12.345.678/0001-90", "email": "financeiro@ibi.com.br",   "cidade": "São Paulo, SP", "categoria": "Fornecedor",    "ativo": True},
    {"id": 2, "nome": "Maria Helena de Souza",                "tipo": "pessoa_fisica",   "doc": "123.456.789-00",     "email": "maria.helena@email.com",  "cidade": "Rio Verde, GO", "categoria": "Cliente",       "ativo": True},
    {"id": 3, "nome": "Transportes Rodoplan Ltda",            "tipo": "pessoa_juridica", "doc": "98.765.432/0001-12", "email": "contato@rodoplan.com",    "cidade": "Goiânia, GO",   "categoria": "Fornecedor",    "ativo": True},
    {"id": 4, "nome": "João Carlos Pereira",                  "tipo": "pessoa_fisica",   "doc": "987.654.321-00",     "email": "joao.pereira@email.com",  "cidade": "Brasília, DF",  "categoria": "Funcionário",   "ativo": True},
    {"id": 5, "nome": "AgroTech Soluções Digitais",           "tipo": "pessoa_juridica", "doc": "45.678.901/0001-34", "email": "sac@agrotech.com",        "cidade": "Curitiba, PR",  "categoria": "Fornecedor",    "ativo": False},
    {"id": 6, "nome": "Cooperativa de Crédito Sicoob",        "tipo": "pessoa_juridica", "doc": "11.222.333/0001-44", "email": "atendimento@sicoob.com",  "cidade": "Goiânia, GO",   "categoria": "Instituição",   "ativo": True},
]

# ----------------------------------------------------------------------
# fin_titulo
# ----------------------------------------------------------------------
TITULOS = [
    {"id": 1, "numero": "TIT-2026-0142", "descricao": "Compra de fertilizantes - Lote 4521",  "natureza": "despesa", "favorecido": "Indústria Brasileira de Insumos S.A.", "vencimento": "2026-04-28", "valor":  84500.00, "pago":      0.00, "status": "aberto",    "categoria": "Insumos Agrícolas"},
    {"id": 2, "numero": "TIT-2026-0141", "descricao": "Venda de soja - Contrato #8821",        "natureza": "receita", "favorecido": "Trading Internacional Brasil",         "vencimento": "2026-04-25", "valor": 240000.00, "pago": 240000.00, "status": "pago",      "categoria": "Vendas"},
    {"id": 3, "numero": "TIT-2026-0140", "descricao": "Frete coletivo - Safra 25/26",          "natureza": "despesa", "favorecido": "Transportes Rodoplan Ltda",            "vencimento": "2026-04-15", "valor":  12750.50, "pago":      0.00, "status": "atrasado",  "categoria": "Logística"},
    {"id": 4, "numero": "TIT-2026-0139", "descricao": "Folha de pagamento - Abril",            "natureza": "despesa", "favorecido": "João Carlos Pereira",                  "vencimento": "2026-05-05", "valor":   8450.00, "pago":      0.00, "status": "aberto",    "categoria": "Pessoal"},
    {"id": 5, "numero": "TIT-2026-0138", "descricao": "Mensalidade software de gestão",        "natureza": "despesa", "favorecido": "AgroTech Soluções Digitais",           "vencimento": "2026-04-30", "valor":   1899.00, "pago":   1899.00, "status": "pago",      "categoria": "Tecnologia"},
    {"id": 6, "numero": "TIT-2026-0137", "descricao": "Recebimento parcial - Cliente Maria H.","natureza": "receita", "favorecido": "Maria Helena de Souza",                "vencimento": "2026-04-20", "valor":   5400.00, "pago":   2700.00, "status": "parcial",   "categoria": "Vendas"},
    {"id": 7, "numero": "TIT-2026-0136", "descricao": "Manutenção de maquinário pesado",       "natureza": "despesa", "favorecido": "Mecânica Diesel Total",                "vencimento": "2026-05-10", "valor":  18200.00, "pago":      0.00, "status": "aberto",    "categoria": "Manutenção"},
    {"id": 8, "numero": "TIT-2026-0135", "descricao": "Cancelado - Pedido #4421",              "natureza": "despesa", "favorecido": "Distribuidora Nacional",               "vencimento": "2026-04-12", "valor":   3200.00, "pago":      0.00, "status": "cancelado", "categoria": "Outros"},
]

# ----------------------------------------------------------------------
# fin_banco / fin_conta_bancaria (achatados para listagem)
# ----------------------------------------------------------------------
BANCOS = [
    {"id": 1, "codigo": "001", "nome": "Banco do Brasil",  "agencia": "1234-5", "conta": "12345-6", "tipo": "Conta Corrente", "saldo":  428500.10, "ativo": True},
    {"id": 2, "codigo": "756", "nome": "Sicoob",           "agencia": "0987-1", "conta": "78901-2", "tipo": "Conta Corrente", "saldo":  312450.00, "ativo": True},
    {"id": 3, "codigo": "237", "nome": "Bradesco",         "agencia": "4567-8", "conta": "55432-1", "tipo": "Conta Poupança", "saldo":  185000.00, "ativo": True},
    {"id": 4, "codigo": "341", "nome": "Itaú",             "agencia": "2222-3", "conta": "11111-9", "tipo": "Conta Corrente", "saldo":  125320.32, "ativo": True},
    {"id": 5, "codigo": "260", "nome": "Nubank",           "agencia": "0001",   "conta": "98765-4", "tipo": "Conta Digital",  "saldo":   58450.00, "ativo": True},
    {"id": 6, "codigo": "748", "nome": "Sicredi",          "agencia": "3030-1", "conta": "44455-6", "tipo": "Conta Corrente", "saldo":   12750.00, "ativo": False},
]
