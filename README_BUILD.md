# Como Criar o Executável do Sistema CRM Compressores

## Pré-requisitos
- Python 3.8 ou superior instalado
- Windows 10 ou superior

## Passos para Criar o Executável

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar o Build
```bash
# Opção 1: Usar o script automático
build.bat

# Opção 2: Executar manualmente
python build_executable.py
pyinstaller --clean Sistema_CRM_Compressores.spec
```

### 3. Localizar o Executável
O executável será criado em: `dist/Sistema_CRM_Compressores.exe`

## Funcionalidades Incluídas no Executável
- ✅ Todos os módulos do sistema
- ✅ Imagens e recursos visuais
- ✅ Geradores de PDF
- ✅ Banco de dados SQLite
- ✅ Sistema de permissões
- ✅ Interface gráfica completa

## Distribuição
Para usar em outro computador:
1. Copie a pasta `dist` completa
2. Execute `Sistema_CRM_Compressores.exe`
3. Não é necessário instalar Python

## Solução de Problemas
- Se o executável não abrir, verifique se todas as dependências foram instaladas
- Se houver erro de módulo não encontrado, adicione ao arquivo .spec
- Para debug, use `console=True` no arquivo .spec
