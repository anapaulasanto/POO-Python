class Contato:
  def __init__(self, nome, telefone):
      self.nome = nome
      self.telefone = telefone

  def exibir_info(self):
      texto = f' Nome: {self.nome}\n Número: {self.telefone}'
      print(texto)


class ContatoProfissional(Contato):
  def __init__(self, nome, telefone, empresa, cargo):
      super().__init__(nome, telefone)
      self.empresa = empresa
      self.cargo = cargo

  def exibir_info(self):
      super().exibir_info() 
      print(f' Cargo: {self.cargo}\n Empresa: {self.empresa}')

class ContatoPessoal(Contato):
  def __init__(self, nome, telefone, aniversario):
      super().__init__(nome, telefone)
      self.aniversario = aniversario

  def exibir_info(self):
      super().exibir_info() 
      print(f' Data de aniversário: {self.aniversario}')
      


class Agenda:
    def __init__(self):
        self.contatos = [] #cria lista vazia

    def adicionar_contato(self,contato):
        self.contatos.append(contato)  #adiciona o parametro/objeto contato na lista

    def exibir_contato(self):
        if not self.contatos:
            print('\nA agenda está vazia.')

        else:
            for x in self.contatos:  #percorre a lista
                print('--------------------------------------')
                x.exibir_info()  #pra cada x percorrido na lista eu chamo o metodo exibir_info q vai se adaptar ao objeto instanciado
                print('--------------------------------------')


"""agenda = Agenda()  #instanciando a classe Agenda() com o objeto agenda

contato1 = ContatoPessoal("Livia", "859999999", "26 de maio") #objeto contato1 do tipo ContatoPessoal que passa os valores dos atributos
contato2 = ContatoProfissional("Ana", "859999999", "Unichristus", "Desenvolvedora")

agenda.adicionar_contato(contato1)  #chama o metodo adicionar_contato do objeto agenda
agenda.adicionar_contato(contato2)

agenda.exibir_contato() #chama o metodo exibir_contato do objeto agenda
"""

def obter_tipo_contato(tipo_contato):

    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')

    if tipo_contato == 'pessoal':
        aniversario = input('Informe a data de aniversário: ')
        return ContatoPessoal(nome, telefone,aniversario)
    
    elif tipo_contato == 'profissional':
        empresa = input('Digite o nome da empresa: ')
        cargo = input('Digite o cargo na empresa: ')
        return ContatoProfissional(nome,telefone,empresa,cargo)
    
    else:
        print('Tipo de contato inválido')
        return None

agenda = Agenda()

print('------------------ AGENDA DE CONTATOS -------------------------')

while True:
    print('\nOpções:')
    print('1. Adicionar contato')
    print('2. Exibir contatos')
    print('3. Sair')

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        tipo_contato = input("Escolha o tipo de contato (pessoal ou profissional): ").lower()
        novo_contato = obter_tipo_contato(tipo_contato)
        if novo_contato:
            agenda.adicionar_contato(novo_contato)

    elif opcao == '2':
        agenda.exibir_contato()

    elif opcao == '3':
        break

    else:
        print("Opção inválida. Tente novamente.")
