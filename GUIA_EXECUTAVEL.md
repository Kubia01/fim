# 🚀 GUIA COMPLETO - CRIAR EXECUTÁVEL DO SISTEMA CRM COMPRESSORES

## 📋 Pré-requisitos
- **Windows 10 ou superior**
- **Python 3.8 ou superior** (apenas para criar o executável)
- **Conexão com internet** (para instalar dependências)

## 🔧 Passos para Criar o Executável

### 1. Instalar Dependências
Abra o **Prompt de Comando** ou **PowerShell** como administrador e execute:

```bash
pip install -r requirements.txt
```

### 2. Criar o Executável
Execute o script de build:

```bash
build.bat
```

**OU** execute manualmente:

```bash
python build_executable.py
pyinstaller --clean Sistema_CRM_Compressores.spec
```

### 3. Testar o Executável
Execute o script de teste:

```bash
testar_executavel.bat
```

### 4. Preparar para Distribuição
Execute o script de distribuição:

```bash
preparar_distribuicao.bat
```

## 📁 Estrutura de Arquivos Criados

```
Sistema_CRM_Compressores_Distribuicao/
├── Sistema_CRM_Compressores.exe    # Executável principal
├── assets/                         # Imagens e recursos
├── interface/                      # Módulos da interface
├── pdf_generators/                 # Geradores de PDF
├── utils/                          # Utilitários
├── database.py                     # Banco de dados
├── cabeçalho.jpeg                  # Imagem do cabeçalho
├── caploc.jpg                      # Imagem da capa
└── LEIA-ME.txt                     # Instruções de uso
```

## ✅ Funcionalidades Incluídas no Executável

### 🔐 Sistema de Login
- Autenticação de usuários
- Controle de permissões
- Usuário padrão: **admin/admin**

### 👥 Gestão de Clientes
- Cadastro completo de clientes
- Múltiplos contatos por cliente
- Busca automática de CEP
- Validação de CNPJ e e-mail

### 📦 Gestão de Produtos/Serviços
- Cadastro de produtos e serviços
- Criação de kits (composição)
- Controle de ativo/inativo
- Validação de dados

### 💼 Cotações e Locações
- Criação de cotações
- Gestão de locações
- Cálculos automáticos
- Status de cotações

### 📊 Relatórios
- Relatórios técnicos
- Geração de PDFs
- Exportação de dados
- Dashboard com estatísticas

### 🔐 Sistema de Permissões
- Controle de acesso por módulo
- Usuários com permissão "Consultar" (somente leitura)
- Usuários com permissão "Controle Total" (edição completa)
- **NOVO**: Listas suspensas bloqueadas para usuários "Consultar"

## 🚀 Como Usar o Executável

### 1. Executar o Sistema
- Execute: `Sistema_CRM_Compressores.exe`
- O sistema criará o banco de dados automaticamente
- Use as credenciais: **admin/admin**

### 2. Primeiro Uso
- O sistema criará automaticamente:
  - Banco de dados SQLite
  - Usuário administrador padrão
  - Estrutura de tabelas

### 3. Funcionalidades Disponíveis
- **Dashboard**: Visão geral do sistema
- **Clientes**: Gestão completa de clientes
- **Produtos**: Cadastro de produtos e serviços
- **Cotações**: Criação e gestão de cotações
- **Relatórios**: Geração de relatórios técnicos
- **Usuários**: Gestão de usuários e permissões

## 📦 Distribuição

### Para Usar em Outro Computador:
1. Copie a pasta `Sistema_CRM_Compressores_Distribuicao` completa
2. Execute `Sistema_CRM_Compressores.exe`
3. **NÃO é necessário instalar Python**

### Requisitos do Computador de Destino:
- Windows 10 ou superior
- **NÃO precisa de Python instalado**
- **NÃO precisa de dependências**

## 🔧 Solução de Problemas

### Se o Executável Não Abrir:
1. Verifique se o Windows Defender não está bloqueando
2. Execute como administrador
3. Verifique se todos os arquivos foram copiados

### Se Houver Erro de Módulo:
1. Verifique se o arquivo `.spec` inclui o módulo
2. Adicione o módulo ao `hiddenimports` no arquivo `.spec`

### Para Debug:
1. Edite o arquivo `.spec`
2. Mude `console=False` para `console=True`
3. Recompile o executável

## 📋 Scripts Disponíveis

| Script | Função |
|--------|--------|
| `build.bat` | Criar executável |
| `testar_executavel.bat` | Testar executável |
| `preparar_distribuicao.bat` | Preparar para distribuição |
| `limpar_temporarios.bat` | Limpar arquivos temporários |

## 🎯 Resultado Final

O executável criado terá **EXATAMENTE** as mesmas funcionalidades do sistema que você usa no VS Code:

✅ **Interface gráfica completa**
✅ **Todos os módulos funcionais**
✅ **Sistema de permissões**
✅ **Geração de PDFs**
✅ **Banco de dados SQLite**
✅ **Imagens e recursos visuais**
✅ **Todas as funcionalidades de edição**
✅ **Sistema de login e autenticação**

## 🚀 Próximos Passos

1. Execute `build.bat` no seu computador Windows
2. Aguarde a compilação (pode demorar alguns minutos)
3. Teste com `testar_executavel.bat`
4. Prepare a distribuição com `preparar_distribuicao.bat`
5. Copie a pasta de distribuição para outro computador
6. Execute `Sistema_CRM_Compressores.exe` no computador de destino

**🎉 Pronto! Seu sistema estará funcionando em qualquer computador Windows sem precisar instalar Python!**