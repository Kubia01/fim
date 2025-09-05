@echo off
echo ========================================
echo    PREPARANDO DISTRIBUICAO
echo ========================================
echo.

echo [1/3] Criando pasta de distribuicao...
if exist "Sistema_CRM_Compressores_Distribuicao" (
    rmdir /s /q "Sistema_CRM_Compressores_Distribuicao"
)
mkdir "Sistema_CRM_Compressores_Distribuicao"

echo.
echo [2/3] Copiando arquivos...
xcopy "dist\*" "Sistema_CRM_Compressores_Distribuicao\" /E /I /Y

echo.
echo [3/3] Criando arquivo de instrucoes...
echo Sistema CRM Compressores > "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo. >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo INSTRUCOES DE USO: >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo. >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo 1. Execute: Sistema_CRM_Compressores.exe >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo 2. Use as credenciais: admin/admin >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo 3. O sistema criara o banco de dados automaticamente >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo 4. Todas as funcionalidades estao disponiveis >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo. >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo FUNCIONALIDADES INCLUIDAS: >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Gestao de Clientes >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Gestao de Produtos/Servicos >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Cotações e Locacoes >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Relatorios Tecnicos >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Sistema de Permissoes >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Geracao de PDFs >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo. >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo REQUISITOS: >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Windows 10 ou superior >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"
echo - Nao e necessario instalar Python >> "Sistema_CRM_Compressores_Distribuicao\LEIA-ME.txt"

echo.
echo ✅ Distribuicao preparada em: Sistema_CRM_Compressores_Distribuicao
echo.
echo 📁 Para distribuir, copie a pasta completa para outro computador
echo 🚀 Execute: Sistema_CRM_Compressores.exe
echo.
echo ========================================
echo    DISTRIBUICAO CONCLUIDA
echo ========================================
pause
