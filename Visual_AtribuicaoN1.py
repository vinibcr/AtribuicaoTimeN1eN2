from datetime import datetime, timedelta
import requests
import json
import schedule
import threading
import time
import tkinter as tk
import openpyxl
from openpyxl import load_workbook

# Configurações do Jira
jira_url = 'https://.atlassian.net'  # URL base do Jira
username = 'vinicius'
api_token = '_GZ7fCn3QbCJLsCE112XhnMw=B64FAFE5'
filter_id = ''  # ID do filtro JQL que contém os chamados

# Dicionário com horários de entrada dos analistas
analistas = {
    # Configurações dos analistas (email e horários de entrada e almoço)
}

# Lista para armazenar os chamados já distribuídos
chamados_distribuidos = []

# Lista de Logs
logs = []

# Arquivo para armazenar o índice do último analista utilizado
arquivo_indice_analista = 'ultimo_indice_analista.txt'

# Variável global para controle da execução do programa
programa_em_execucao = True

# Função para buscar os issues de um filtro
def buscar_chamados_do_filtro(filter_id):
    # #comentario: Busca os chamados do Jira usando um filtro JQL e retorna suas chaves
    pass

# Função para obter o accountId do usuário a partir do email
def get_account_id(assignee_email):
    # #comentario: Obtém o accountId de um usuário a partir do email
    pass

#Função que busca histórico do chamado para verificar se o mesmo ja foi passado para algum analista presente para atribuir
def obter_historico_chamado(issue_key):
    # #comentário: Obtém a chave, e busca o histórico. Retornando uma lista de analistas que interagiram no chamado

# Função para obter o ID da primeira transição de status disponível
def get_first_transition_id(issue_key):
    # #comentario: Obtém o ID da primeira transição de status disponível para um chamado
    pass

# Função para adicionar um comentário
def adicionar_comentario(issue_key, comentario):
    # #comentario: Adiciona um comentário a um chamado específico
    pass

# Função para atualizar o status do issue
def update_status(issue_key, transition_id):
    # #comentario: Atualiza o status de um chamado para uma transição específica
    pass

# Função para obter o status atual do issue
def get_issue_status(issue_key):
    # #comentario: Obtém o status atual de um chamado
    pass

# Função para atualizar o assignee do issue
def update_assignee(issue_key, account_id):
    # #comentario: Atualiza o assignee de um chamado para um usuário específico
    pass

# Função para distribuir chamados entre os analistas
def distribuir_chamados(issue_keys, analistas):
    # #comentario: Distribui chamados entre os analistas disponíveis
    pass

# Função para verificar se há chamados no filtro e iniciar o processo de distribuição
def verificar_chamados_e_iniciar_processo():
    # #comentario: Verifica se há chamados e inicia o processo de distribuição
    pass

# Função para salvar os logs em um arquivo Excel
def salvar_logs_excel():
    # #comentario: Salva os logs de distribuição de chamados em um arquivo Excel
    pass

# Função para fechar completamente o programa
def fechar_programa():
    # #comentario: Fecha o programa e salva os logs
    pass

# Função para rodar o programa
def rodar_programa():
    # #comentario: Inicia o processo de verificação e distribuição de chamados periodicamente
    pass

# Função para iniciar a interface gráfica
def iniciar_interface():
    # #comentario: Inicia a interface gráfica do usuário (GUI) para controlar o programa
    pass

def main():
    # #comentario: Inicia a interface gráfica em uma thread separada
    gui_thread = threading.Thread(target=iniciar_interface)
    gui_thread.start()

if __name__ == "__main__":
    main()
