"""
    Simulação da Artilharia Copa do Mundo FIFA 2026

"""

"""Utilizando , Import os = Ele importa a biblioteca 
e limpa o terminal"""

import os 
print(os.getcwd())
print("Pasta atual:", os.getcwd())
print("Arquivo existe?", os.path.exists("jogadores.json"))
import json

"""Carregando o arquivo json para o python
"""
with open("jogadores.json", "r") as arquivo:
    jogadores = json.load(arquivo)

"""

Função 1: limpar_tela()

Limpa toda a tela do terminal para manter um  programa limpo

"""

def limpar_tela():
    import os
    os.system('cls')

"""

FUNÇÃO 2: mostrar_menu()

"""

def mostrar_menu():
    
    
    limpar_tela()
    

    
    print('=' * 50)

    print('Artilharia Copa do Mundo FIFA 2026')

    print('=' * 50)

    print('1) Adicionar jogador. ')
    print('2) Buscar jogador. ')
    print('3) Atualizar número de gols. ')
    print('4) Remover jogador. ')
    print('5) Mostrar lista completa de artilharia. ')
    print('0) Sair do sistema. ')

    print('=' * 50)

"""Loop do menu principal , ficara repetindo até que o usuário
opte em sair do menu. """

while True:

    mostrar_menu()
    

    opcao = input('Digite sua opção (0-5): ').strip()

    if opcao == '0':
        
        limpar_tela()
        
        print('=' * 50)
        
        print('Obrigado por usar o sistema !')
        
        print('=' * 50)
        
        """ Utilizando Enter foi incrementada uma função para 
        confirma a saída do programa. """
        
        input('\nPressione Enter para encerrar o programa ! ')
        

        break 
  
  
        """ Opção 1: CADASTRAR UM NOVO JOGADOR (CREATE) """

    elif opcao == '1':
        
        print('\nCADASTRAR NOVO JOGADOR. ')
        
        print('-' * 30)

        """ 
        
        Para o cadastro de um jogador é solicitado
        o nome completo.
        
        .lower () - Não descrimina letras maiúsculas ou minúsculas.
        .strip () - Não descrimina espaços extras.
        
        """
        nome = input('Nome completo: ').lower().strip()
        
        """ Caso o nome jogador não estaja na lista,TRUE/False = 
        O tratamento de erro """
        nome_existe = False
        
        for jogador in jogadores:
            if jogador['nome'] == nome:
                nome_existe = True
                break
        
        """

        Caso o usuário já tenha cadastrado o nome deste jogador
        informar que o nome já está cadastrado.
        .title ()  - Utilizado para transformar a primeira letra sempre em Maiúscula.

        """
        
        if nome_existe:
            print(f'{nome.title()} já está cadastrado!')
        
           
            """Será criado um dicionário , para acumular os dados
            de novos jogadores. """
        
        else:
            
            novo_jogador = {
        'nome': nome,  
        'posicao': input('Posição (ex: atacante): ').lower().strip(),
        'gols': int(input('Número de gols: ')),  
        'selecao': input('Seleção (ex: Brasil): ').strip()
    }

            """ Irei adiconar este jogador a lista , de dicionário .
            E então em seguida retornar ao menu. """

            jogadores.append(novo_jogador)
            print('Jogador adicionado à artilharia com sucesso!')



        input('\nPressione Enter para voltar ao menu ! ')

        """ Opção 2.
        
        Buscar jogador pelo nome.
            
        """

    elif opcao == '2':
        
        print('\nBUSCA DE JOGADOR')
        
        print('-' * 30)

        """ Na Opção 2 . Iremos perguntar o nome que o User deseja encontrar. 
        Utilizamos FOR para buscar na lista o nome do jogador."""

        nome_busca = input('Qual jogador deseja encontrar : ').lower().strip()
        encontrado = False  
        
        for jogador in jogadores:

            """ Caso o nome do jogador esteja na lista.
                Mostrar todos os dados deste jogador. """
                
                
            if jogador['nome'] == nome_busca:

                """ Caso o jogador seja encontrado, todos os dados 
                    solicitados deste jogador seram imprimidos
                    e o break é acionado. """
                
                print('\nJOGADOR ENCONTRADO:')
                
                print(f'Nome: {jogador["nome"].title()}')
                print(f'Posição: {jogador["posicao"].title()}')
                print(f'Gols: {jogador["gols"]}')
                print(f'Seleção: {jogador["selecao"]}')
                
                
                encontrado = True
                break 
        
        """ E se o jogador não for encontrado o user deverá
            retornar ao menu """
        
        if not encontrado:
            
            print('Jogador não encontrado na artilharia ! ')

        input('\nPressione Enter para voltar ! ')

        """ Opção 3 . É conhecida como (UPDATE), a atualização. """
    
    elif opcao == '3':
        print('\nATUALIZAR NÚMERO DE GOLS')
        print('-' * 30)


        """ Para que ocorra essa atualização é solicitado
            ao User, qual o nome do jogador , que este
            deseja atualizar. """

        nome = input('Nome do jogador: ').lower().strip()

        """ Com FOR eu busco na lista de Jogadores, o nome que o User
        decidiu fazer a alteração. Lembrando que está alteração, 
        é apenas no número de gols, dado que é solicitado ao User.
        Feito isso o Break, é acionado e o User , retorna ao menu. """
        
        
        for jogador in jogadores:
            if jogador['nome'] == nome:
               
                novos_gols = int(input('Novos gols: '))
                jogador['gols'] = novos_gols
                print('Gols atualizados!')
                
                
                break  
            
            """ Caso o User venha digitar um nome inesxistente.
                Utilizando uma condição ELSE. A tratação de erro 
                tem o seguinte resultado. (print) e após o User retorna
                ao menu principal. """
        else:
           
            print('Jogador não encontrado!')

        input('\nPressione Enter para voltar...')

            
        """ Iniciando a opção 4: Que será o (DELETE)
            Nesta opção o user poderá deletar um jogador.
            
            EX. User colocou um número onde deveria conter apenas letras.
            Neste caso o User poderá excluir o jogador e adicionar novamente
            de forme correta."""
            
    
    elif opcao == '4':
        print('\nREMOVER JOGADOR')
        print('-' * 30)
        nome = input('Nome para remover: ').lower().strip()
        
        """ A solicitação será apenas o nome do jogador para remover. 
            Estamos utilizando (ENUMERATE) para ter o índice e os dados do jogador."""

        for i, jogador in enumerate(jogadores):
            if jogador['nome'] == nome:
                
                """ Iremos mostrar o jogador que será removido e em seguida.
                Será solicitado ao user a confirmação da exclusão."""
                
                print('\nConfirmar remoção:')
                print(f'  {jogador["nome"].title()} - {jogador["gols"]} gols')
                confirm = input('Confirmar? (s/n): ').lower()
                
                """ A partir da da condição que o user escolheu o jogador pode
                ter seu nome e dados excluso da lista de artilharia. 
                Ou a condição do User foi (N) e a escolha foi cancelada. """
                
                if confirm == 's':
                    del jogadores[i]
                    print('Jogador removido da artilharia!')
                else:
                    print('Remoção cancelada.')
                break  
            
            """ Ou se o User digitar um nome inesistente. 
                Este será informado e voltará ao menu principal. """
            
        else:
            print('Jogador não encontrado!')

        input('\nPressione Enter para voltar...')

        """ Na opção : 5 o User poderá visualizar toda a 
            lista de artilharia que foi criada.
            E caso não tenha nenhum jogador cadastrado
            este também será informado. """ 
        
    elif opcao == '5':
      
        limpar_tela()
        print('Artilharia Completa (ordenada por gols)')
        print('=' * 60)
        if not jogadores:
            print('Nenhuma artilharia cadastrada!')
            
            """Será necessário ordena a lista de jogadores por número de gols 
            do maior para menor, para isso irei utilizar a função (key=lambda )
            utilizando o critério em gols. 
            
            Onde irá ordenar pelo valor de gols de cada jogador.
            
            E reverse=True inverte a ordem do maior para o menor. """
        
        else:
 
            artilharia_ordenada = sorted ( jogadores,
            key=lambda x: x['gols'],  
            reverse=True )
           
            """ Utilizando a formatação em cada campo do jogador 
                Exibir a lista completa com todos os dados do jogador. """
        
            numero = (f'{i:2d}.')             
            nome = (f'{jogador["nome"].title()}') 
            gols = (f'{jogador["gols"]:2d}')  
            posicao = (f'{jogador["posicao"].title()}')
            selecao = (jogador["selecao"])

            
            print(f'{numero} {nome} | {gols} gols | {posicao} | {selecao}')
                
        print('=' * 60)
        input('\nPressione Enter para voltar ao menu...')

        """ Caso o User venha digitar uma opção invalida
            Imprimir o erro na tela. E retornar ao menu. """
            
    else:
        print('Opção inválida! Digite um número de 0 a 5.')
        input('Pressione Enter para tentar novamente...')

    """Um último aviso ao User de que ele realmente saiu do programa. """

print('Programa encerrado.')


