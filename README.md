**Projeto Sistema Distribuídos**

**Ideia inicial** *IPromotion*:
A ideia e criar uma aplicação que fornece ao público promoções (*Gift cards/ descontos*) diárias de empresas que queiram divulgar seus produtos em promoção. 

**Funcionamento**:
Nela a empresa pode inserir promoções, atualizar e deletar de acordo como for conveniente, para que fique salvo no banco de dados da aplicação para
que seja notificado ao cliente.
Nela o cliente também deve fazer um cadastro para que seus dados fiquem salvos, para que possam receber as notificações.
Quando a empresa desejar promover suas promoções, ela apertará um botão e todos os clientes cadastrados no banco de dados serão notificados com um pop-up em sua tela.

**Ferramentas**:
* A aplicação será toda implementada em JavaScript usando para o Backend: NodeJS e para o Frontend: ReactJS.
* Todos os dados serão salvos em um banco NoSQL: MongoDB, usando Mongoose.
* O servidor será criado usando Express.

**Componentes**
 * Empresa  (*Ainda não sei as quantidades*)
 * Cliente  (*Ainda não sei as quantidades*)
 * Aplicativo
 * Servidor
 * Banco de Dados

**Testes**
* Demonstração de funcionalidades: mostrar que as funcionalidades de CRUD (*Create, Read, Update, Delete*) foram implementadas.
* Teste de concorrência: mostrar que multiplas empresas e clientes possam acessar a aplicação ao mesmo tempo.
* Teste de recuperação de falhas: mostrar que se a aplicação falhar, quando voltar a executar não haverá nenhum estado inesperado.
* Teste de carga: fazer a verificação de dados que uma empresa consegue guardar no banco e o quanto de dados o cliente consegue receber.
