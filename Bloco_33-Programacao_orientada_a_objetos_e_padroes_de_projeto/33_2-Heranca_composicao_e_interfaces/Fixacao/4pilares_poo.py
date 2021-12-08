# Os quatro pilares da Programação Orientada a Objetos
# Na aula anterior falamos de Encapsulamento e Abstração . Dois dos quatro pilares de POO. Nessa aula falamos, sem contar pra você, dos outros dois, então vamos dar o nome aos bois!

# Herança
# A herança, como o próprio nome já diz, é o princípio que define que uma classe deve ser capaz de herdar seus atributos e métodos de outra. E embora a classe base possa ter tanto métodos abstratos (que precisam ser implementados) quanto métodos concretos (que já estão implementados), a boa prática diz que a herança deve ser usada apenas para especialização. Se você quer apenas compartilhar código, use composição.

# Polimorfismo
# Segundo o dicionário, a palavra "polimorfismo" significa "qualidade ou estado de ser capaz de assumir diferentes formas". Em POO, o polimorfismo é caracterizado quando duas ou mais classes contêm implementações diferentes para métodos com a mesma interface. Nos nossos exemplos de hoje pense, por exemplo, no método serialize , que é definido de forma abstrata na classe Serializer e assume diferentes formas nas classes JSONSerializer e CSVSerializer

# Os quatro pilares em uma frase
# Na Programação Orientada a Objetos, você deve criar entidades ( Abstração ) com as mensagens que escuta bem definidas ( Encapsulamento ), podendo especializar comportamentos de entidades ( Herança ) contanto que garanta que a forma de enviar mensagens é consistente ( Polimorfismo )