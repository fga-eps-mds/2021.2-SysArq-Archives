[![Build](https://github.com/fga-eps-mds/2021.2-SysArq-Archives/workflows/Compilação/badge.svg)](https://github.com/fga-eps-mds/2021.2-SysArq-Archives/actions/workflows/build.yml)
[![Style](https://github.com/fga-eps-mds/2021.2-SysArq-Archives/workflows/Estilo/badge.svg)](https://github.com/fga-eps-mds/2021.2-SysArq-Archives/actions/workflows/style.yml)
[![Tests](https://github.com/fga-eps-mds/2021.2-SysArq-Archives/workflows/Testes/badge.svg)](https://github.com/fga-eps-mds/2021.2-SysArq-Archives/actions/workflows/test.yml)

# API de Gerenciamento de Arquivos do SysArq

[![codecov](https://codecov.io/gh/fga-eps-mds/2021.2-SysArq-Archives/branch/main/graph/badge.svg?token=63NX5KPYRZ)](https://codecov.io/gh/fga-eps-mds/2021.2-SysArq-Archives)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=bugs)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=fga-eps-mds_2021.2-SysArq-Archives&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=fga-eps-mds_2021.2-SysArq-Archives)

A API de Gerenciamento de Arquivos do *SysArq* compõe a arquitetura de microsserviços do sistema *[SysArq](https://fga-eps-mds.github.io/2021-2-SysArq-Doc/)*.

Esse microsserviço é responsável pelo *CRUD* ([veja a definição](https://developer.mozilla.org/pt-BR/docs/Glossary/CRUD)), pesquisa e filtragem de documentos. **[Saiba mais](https://fga-eps-mds.github.io/2021-2-SysArq-Doc/documentation/)**

## Execução

### Requisitos
 - ***`Docker`*** - [veja como instalar](https://docs.docker.com/engine/install/);
 - ***`docker-compose`***, no mínimo a versão *`1.29.0`* - [veja como instalar](https://docs.docker.com/compose/install/).

### Executar

1. Clone esse repositório - [veja como clonar um repositório](https://docs.github.com/pt/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository);

2. Crie, utilizando o arquivo ***env-reference***, o *`.env`* dentro da **pasta do repositório**;

3. Execute, dentro da **pasta do repositório**, o comando:
   ```
    sudo docker-compose up
   ```

4. Acesse [http://0.0.0.0:8002/](http://0.0.0.0:8002) no navegador. 

### Testes e Verificação de Estilo

-  Para **testar** a aplicação, utilize o ***pytest***. Por exemplo:
   ```
      sudo docker-compose run web pytest --cov
   ```
   **Observação**: Só serão aceitas contribuições com 90% de cobertura de código.

- Para **verificar o estilo de código** da aplicação, utilize o ***flake8***. Por exemplo:
   ```
      sudo docker-compose run web flake8
   ```
   **Observação**: Só serão aceitas contribuições com o estilo correto.

**ATENÇÃO**: Execute os comandos dentro da **`pasta`** do repositório.

## Documentação

### Como contribuir

- Leia o [guia de contribuição](CONTRIBUTING.md)
