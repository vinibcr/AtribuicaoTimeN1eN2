# AtribuicaoTimeN1eN2
Agilidade e precisão ao envio e gerenciamento dos tickets da minha equipe, composta por cerca de 30 analistas N1 e 6 analistas N2.   O programa tem como objetivo distribuir os chamados pendentes no sistema aos analistas, sendo atualizados a cada 10 minutos automaticamente, além de respeitar a jornada de trabalho de cada funcionário.

buscar_chamados_do_filtro(filter_id)

Obtém uma lista de chamados não resolvidos com base no filtro JQL fornecido.
get_account_id(assignee_email)

Obtém o ID de conta do usuário a partir do seu email.
get_first_transition_id(issue_key)

Obtém o ID da primeira transição de status disponível para um chamado.
adicionar_comentario(issue_key, comentario)

Adiciona um comentário a um chamado específico.
update_status(issue_key, transition_id)

Atualiza o status de um chamado e adiciona um comentário se o status for "Reaberto".
get_issue_status(issue_key)

Obtém o status atual de um chamado.
update_assignee(issue_key, account_id)

Atualiza o responsável (assignee) de um chamado com base no ID da conta.
distribuir_chamados(issue_keys, analistas)

Distribui chamados entre analistas disponíveis, verificando horários de trabalho.
verificar_chamados_e_iniciar_processo()

Verifica se há chamados no filtro e inicia o processo de distribuição.
salvar_logs_excel()

Salva os logs de distribuição de chamados em um arquivo Excel.
fechar_programa()

Finaliza o programa, salva logs e fecha a interface gráfica.
rodar_programa()

Inicia o processo de distribuição de chamados em um intervalo regular e encerra o programa ao final do dia.
iniciar_interface()

Cria e exibe a interface gráfica para controlar a execução do programa.
main()

Inicia a interface gráfica em um novo thread.
