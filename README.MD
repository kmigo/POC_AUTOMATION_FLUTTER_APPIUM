**Descrição do Repositório para POC de Testes Automatizados em Flutter:**

---

### Título: 
POC - Testes Automatizados em Flutter com Appium

### Descrição: 

Este repositório contém uma Prova de Conceito (POC) para a implementação de testes automatizados em um projeto Flutter utilizando o Appium. O objetivo é validar a eficácia e a eficiência dos testes automatizados em uma aplicação Flutter, utilizando o Python como linguagem de script de teste.

### Configuração do Ambiente:

1. **Instalação do Appium**:
   ```bash
   npm install -g appium@2.0.0-beta.44
   ```

2. **Instalação das Dependências Python**:
   ```bash
   pip install Appium-Flutter-Finder==0.4.0 pytest==6.2.4 pytest-order==1.1.0 pytest-dependency==0.5.1
   ```

### Configuração do Projeto Flutter:

1. **Atualização do arquivo `pubspec.yaml`**:
   Adicione a seguinte dependência em `dev_dependencies`:
   ```yaml
   flutter_driver:
     sdk: flutter
   ```

2. **Atualização do arquivo `main.dart`**:
   Importe o pacote `flutter_driver/driver_extension.dart` e habilite a extensão Flutter Driver quando estiver no modo de perfil (`kProfileMode`).
   ```dart
   import 'package:flutter/material.dart';
   import 'package:flutter_driver/driver_extension.dart';

   void main() {
     if (kProfileMode) {
       enableFlutterDriverExtension();
     }
     runApp(MyApp());
   }
   ```

3. **Construindo o Aplicativo**:
   ```bash
   flutter build apk --profile
   ```

### Execução dos Testes:

1. **Inicie o Appium**.
2. **Inicie o Emulador Android**. 
   - Certifique-se de que o ADB está instalado e configurado corretamente.
3. **Execute os Testes**:
   - Navegue até o diretório raiz do seu projeto.
   - Certifique-se de que os scripts de teste estão na pasta `test/`.
   - Execute o comando:
     ```bash
     pytest
     ```

Ao seguir as instruções e configurações fornecidas, você será capaz de executar os testes automatizados no seu projeto Flutter, validando assim a integridade e o comportamento desejado do aplicativo.