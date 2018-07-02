## Banco de Dados de Música!

### Introdução:
Este trabalho foi desenvolvido para a Disciplina de 'Programação de Computadores 1' no Instituto de Computação da Universidade Federal Fluminense.

Com o objetivo de estimular a prática dos conceitos aprendidos em aula, foi proposta a realização de um pequeno Banco de Dados usando Python 3. Elementos Básicos da Linguagem, Estruturas de Controle e Repetição, elementos de Programação Procedural (e um pouquinho de OO) estão presentes nesse trabalho.

### Estrutura do programa:
O *Source Code* do programa foi dividido em três arquivos: *data.py*, *main.py*, *style.py*. Essa divisão foi inspirada no modelo MVC e pretende ser uma experimentação dessa abordagem de Engenharia de Software.

No arquivo *style.py* ficam os elementos que são primariamente recursos de exibição e de manipulação de formatação, além de interação com o usuário.
No arquivo *main.py* tem-se o controle do fluxo do programa, com suas principais estruturas. Aqui é onde as ferramentas dos outros arquivos são utilizadas para alcançar o resultado desejado, ao mesmo tempo que isola tais componentes.
No arquivo *data.py* estão as ferramentas que manipulam os arquivos, Mapas e Listas demandadas pelo projeto. Boa parte das soluções criadas para as funcionalidades requeridas se encontram aqui.

### Instruções de Uso:
O processo é bem simples em sistemas Linux(Ubuntu): basta executar o comando "$ python3 main.py" no Terminal e o Menu do programa deve ser aberto. Recomenda-se que o *software* seja utilizado em emuladores de terminal desacoplados de IDE's e Editores de Texto, uma vez que costumam apresentar melhor compatibilidade com os recursos de customização gráfica utilizados. Ainda que o terminal usado seja incompatível com alguns recursos, as funcionalidades primárias não devem ser afetadas.

### Apontamentos sobre o Projeto:
Foram utilizadas 'apenas' quatro colunas de informação, pois há intenção de fazer uso pessoal deste programa como um repositório de Músicas, e a adição de mais colunas de informação seriam desnecessárias para o uso pretendido futuramente. Além disso, a Opção '8' atualmente só filtra os campos 'Banda' e 'Gênero', uma vez que (1) o tempo ficou curto e (2) não consegui pensar em nenhum critério nesses campos que fosse, de fato, prático para a utilização do programa.

Ao abrir o código, é perceptível que alguns trechos do projeto receberam mais 'atenção' que outros por conta de maior refinamento da exibição ou por conter tratamento de erros e verificações de informação inserida. A razão disso foi o tempo estipulado para desenvolver o Banco de Dados e sua proximidade com as Provas Semestrais. A ideia era fazer uma implementação uniforme das funcionalidades, mas ter tido mais trabalho em algumas delas pelo menos demonstra a intenção e o grau de domínio dos recursos oferecidos pelo *Python*.

Por fim, desenvolver esse pequeno projeto foi um desafio bem interessante (afinal, primeiro programa que divido em arquivos, além de somar mais de 500 linhas ao todo) e que deve ser aprimorado como Hobby e prática de Programação e Python. *Feedback* é bem-vindo! :)