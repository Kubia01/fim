@echo off
echo ========================================
echo    TESTANDO SISTEMA CRM COMPRESSORES
echo ========================================
echo.

echo [1/3] Verificando executavel...
if exist "dist\Sistema_CRM_Compressores.exe" (
    echo ✅ Executavel encontrado!
) else (
    echo ❌ Executavel nao encontrado!
    echo Execute build.bat primeiro
    pause
    exit
)

echo.
echo [2/3] Verificando arquivos necessarios...
if exist "dist\assets" (
    echo ✅ Assets encontrados!
) else (
    echo ❌ Assets nao encontrados!
)

if exist "dist\interface" (
    echo ✅ Interface encontrada!
) else (
    echo ❌ Interface nao encontrada!
)

if exist "dist\pdf_generators" (
    echo ✅ Geradores de PDF encontrados!
) else (
    echo ❌ Geradores de PDF nao encontrados!
)

if exist "dist\utils" (
    echo ✅ Utilitarios encontrados!
) else (
    echo ❌ Utilitarios nao encontrados!
)

echo.
echo [3/3] Executando sistema...
echo 🚀 Iniciando Sistema CRM Compressores...
echo.
echo ⚠️  IMPORTANTE:
echo    - O sistema criara um banco de dados SQLite automaticamente
echo    - Use as credenciais padrao: admin/admin
echo    - Todas as funcionalidades estao disponiveis
echo.

start "" "dist\Sistema_CRM_Compressores.exe"

echo.
echo ========================================
echo    TESTE CONCLUIDO
echo ========================================
pause
