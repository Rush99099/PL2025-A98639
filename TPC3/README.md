Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet
# Conversor de MarkDown para HTML

Bruno Campos  
A98639

## Resumo do funcionamento do programa

Este programa usa expressões regulares para converter os elementos marcantes de MarkDown nos elementos correspondentes de HTML.

## Funcionamento do programa

Cada função antes da função `markdown_to_html` implementa a conversão de headers, bold, italic, numbered lists e links para a sua contrapartida em HTML.
Após isto, o programa usa todas essas funções para retornar todas as linhas do ficheiro ou do texto que estiverem em MarkDown e que foram passadas como argumento.
Por fim este lê o arquivo [input.md](/TPC3/input.md) e converte os dados conforme a sua estrutura (tal como se pode observar no ficheiro de output [output.html](/TPC3/output.html)).

Para executar o programa, basta chamar a função `markdown_to_html()`, caso queira testar com um ficheiro, use a `convert_md_to_html('input.file', 'output.file')`.

P.S.: Lembrando que os headers só são substituídos até ao 3º '#', não sendo substituídos "sub-títulos" depois deste.