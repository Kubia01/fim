@echo off
echo ========================================
echo    BUILDING SISTEMA CRM COMPRESSORES
echo ========================================
echo.

echo [1/4] Instalando dependencias...
pip install pyinstaller
pip install fpdf2
pip install Pillow
pip install openpyxl
pip install matplotlib

echo.
echo [2/4] Criando arquivo de especificacao...
python build_executable.py

echo.
echo [3/4] Compilando executavel...
pyinstaller --clean Sistema_CRM_Compressores.spec

echo.
echo [4/4] Verificando arquivos gerados...
if exist "dist\Sistema_CRM_Compressores.exe" (
    echo ✅ Executavel criado com sucesso!
    echo 📁 Localizacao: dist\Sistema_CRM_Compressores.exe
    echo.
    echo 🚀 Para executar o sistema, execute:
    echo    dist\Sistema_CRM_Compressores.exe
) else (
    echo ❌ Erro ao criar executavel!
)

echo.
echo ========================================
echo    BUILD CONCLUIDO
echo ========================================
pause
