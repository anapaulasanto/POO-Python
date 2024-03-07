class Contato:
  def __init__(self, nome, telefone):
      self.nome = nome
      self.telefone = telefone

  def exibir_info(self):
      texto = f'Nome: {self.nome}\n Número: {self.telefone}'
      print(texto)


class ContatoProfissional(Contato):
  def __init__(self, nome, telefone, empresa, cargo):
      super().__init__(nome, telefone)
      self.empresa = empresa
      self.cargo = cargo

  def exibir_info(self):
      texto = super().exibir_info() + f'\n Cargo: {self.cargo}\n Empresa: {self.empresa}'
      print(texto)

class ContatoPessoal(Contato):
  def __init__(self, nome, telefone, aniversario):
      super().__init__(nome, telefone)
      self.aniversario = aniversario

  def exibir_info(self):
      texto = super().exibir_info() + f'\n Data de aniversário: {self.aniversario}'
      print(texto)


class Agenda:
   def __init__(self):
      self.contatos = [] #cria lista vazia

   def adicionar_contato(self,contato):
      self.contatos.append(contato)  #adiciona o parametro/objeto contato na lista

   def exibir_contato(self):
      for x in self.contatos:  #percorre a lista
         print('--------------------------------------')
         x.exibir_info()  #pra cada x percorrido na lista eu chamo o metodo exibir_info q vai se adaptar ao objeto instanciado
         print('--------------------------------------')


agenda = Agenda()  #instanciando a classe Agenda() com o objeto agenda

contato1 = ContatoPessoal("Livia", "859999999", "26 de maio") #objeto contato1 do tipo ContatoPessoal que passa os valores dos atributos
contato2 = ContatoProfissional("Ana", "859999999", "Unichristus", "Desenvolvedora")

agenda.adicionar_contato(contato1)  #chama o metodo adicionar_contato do objeto agenda
agenda.adicionar_contato(contato2)

agenda.exibir_contato() #chama o metodo exibir_contato do objeto agenda
