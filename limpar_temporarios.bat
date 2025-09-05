@echo off
echo ========================================
echo    LIMPANDO ARQUIVOS TEMPORARIOS
echo ========================================
echo.

echo [1/3] Removendo arquivos de build...
if exist "build" (
    rmdir /s /q "build"
    echo ✅ Pasta build removida
)

if exist "__pycache__" (
    rmdir /s /q "__pycache__"
    echo ✅ Cache Python removido
)

echo.
echo [2/3] Removendo arquivos .pyc...
for /r . %%i in (*.pyc) do del "%%i" 2>nul
echo ✅ Arquivos .pyc removidos

echo.
echo [3/3] Removendo arquivos temporários...
if exist "*.spec" (
    del "*.spec"
    echo ✅ Arquivos .spec removidos
)

echo.
echo ✅ Limpeza concluida!
echo.
echo ========================================
echo    LIMPEZA CONCLUIDA
echo ========================================
pause
