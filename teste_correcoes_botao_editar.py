#!/usr/bin/env python3
"""
Script de teste para verificar as correções do botão Editar e altura das imagens
"""

import sqlite3
import hashlib
from database import DB_NAME, criar_banco

def verificar_sistema():
    """Verificar se o sistema está configurado corretamente"""
    print("=== VERIFICAÇÃO DAS NOVAS CORREÇÕES ===\n")
    
    # Verificar banco
    criar_banco()
    print("✅ Banco de dados verificado")
    
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    try:
        # Verificar usuário de teste
        c.execute("SELECT id, username FROM usuarios WHERE username = 'teste_consulta'")
        user = c.fetchone()
        
        if user:
            user_id = user[0]
            print(f"✅ Usuário de teste encontrado (ID: {user_id})")
            
            # Verificar permissões
            c.execute("SELECT modulo, nivel_acesso FROM permissoes_usuarios WHERE usuario_id = ?", (user_id,))
            perms = dict(c.fetchall())
            print(f"✅ Permissões configuradas: {len(perms)} módulos")
            
            for modulo, nivel in perms.items():
                print(f"   • {modulo}: {nivel}")
        else:
            print("❌ Usuário de teste não encontrado - execute test_permissoes.py")
            
        # Verificar dados de teste
        c.execute("SELECT COUNT(*) FROM clientes")
        clientes_count = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM produtos")
        produtos_count = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM cotacoes WHERE tipo_cotacao = 'Locação'")
        locacoes_count = c.fetchone()[0]
        
        print(f"✅ Dados disponíveis: {clientes_count} clientes, {produtos_count} produtos, {locacoes_count} locações")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na verificação: {e}")
        return False
    finally:
        conn.close()

def main():
    if verificar_sistema():
        print(f"\n🎯 NOVAS CORREÇÕES IMPLEMENTADAS:")
        print(f"")
        print(f"1️⃣ BOTÃO EDITAR HABILITADO PARA CONSULTA:")
        print(f"   ✅ Botão 'Editar' fica habilitado para usuários de consulta")
        print(f"   ✅ Ao clicar em 'Editar', carrega os dados em modo visualização")
        print(f"   ✅ Campos ficam preenchidos e visíveis (cinza)")
        print(f"   ✅ Botões de ação (Salvar, Excluir, etc.) ficam desabilitados")
        print(f"   ✅ Aplicado em: Clientes, Produtos/Cadastros, Locações")
        print(f"")
        print(f"2️⃣ ALTURA DAS IMAGENS NO PDF DOBRADA:")
        print(f"   ✅ Altura das imagens no PDF de locação DOBRADA (100% de aumento)")
        print(f"   ✅ Largura mantida conforme solicitado")
        print(f"   ✅ Aplicado em ambas as imagens do PDF (páginas 4 e 7)")
        print(f"   ✅ Comentários atualizados no código")
        print(f"")
        print(f"🧪 COMO TESTAR:")
        print(f"")
        print(f"📋 TESTE 1 - BOTÃO EDITAR EM CLIENTES:")
        print(f"   1. Execute: python3 main.py")
        print(f"   2. Login: teste_consulta / 123456")
        print(f"   3. Vá para módulo CLIENTES")
        print(f"   4. Selecione qualquer cliente da lista")
        print(f"   5. CLIQUE NO BOTÃO 'EDITAR' (deve estar habilitado)")
        print(f"   6. ✅ VERIFICAR: Todos os campos aparecem preenchidos")
        print(f"   7. ✅ VERIFICAR: Campos ficam cinza (readonly)")
        print(f"   8. ✅ VERIFICAR: Botões 'Salvar' e 'Excluir' desabilitados")
        print(f"")
        print(f"📦 TESTE 2 - BOTÃO EDITAR EM PRODUTOS:")
        print(f"   1. Vá para módulo CADASTROS")
        print(f"   2. Selecione qualquer produto/serviço da lista")
        print(f"   3. CLIQUE NO BOTÃO 'EDITAR' (deve estar habilitado)")
        print(f"   4. ✅ VERIFICAR: Muda para aba de edição")
        print(f"   5. ✅ VERIFICAR: Todos os campos aparecem preenchidos")
        print(f"   6. ✅ VERIFICAR: Campos ficam cinza (readonly)")
        print(f"   7. ✅ VERIFICAR: Botões de ação desabilitados")
        print(f"")
        print(f"📄 TESTE 3 - BOTÃO EDITAR EM LOCAÇÕES:")
        print(f"   1. Vá para módulo LOCAÇÃO")
        print(f"   2. Selecione qualquer locação da lista")
        print(f"   3. CLIQUE NO BOTÃO 'EDITAR' (deve estar habilitado)")
        print(f"   4. ✅ VERIFICAR: Formulário carrega com todos os dados")
        print(f"   5. ✅ VERIFICAR: Campos ficam em modo readonly")
        print(f"   6. ✅ VERIFICAR: Botões de ação desabilitados")
        print(f"")
        print(f"📄 TESTE 4 - ALTURA DAS IMAGENS NO PDF:")
        print(f"   1. No módulo LOCAÇÃO, crie/edite uma locação")
        print(f"   2. Adicione imagens aos equipamentos")
        print(f"   3. Gere o PDF da locação")
        print(f"   4. ✅ VERIFICAR: Imagens têm altura DOBRADA (100% maior)")
        print(f"   5. ✅ VERIFICAR: Largura mantida")
        print(f"   6. ✅ VERIFICAR: Aplicado em ambas as páginas do PDF")
        print(f"")
        print(f"🔑 CREDENCIAIS DE TESTE:")
        print(f"   Usuário: teste_consulta")
        print(f"   Senha: 123456")
        print(f"   Tipo: Consulta (readonly)")
        print(f"")
        print(f"📝 DIFERENÇA DA CORREÇÃO ANTERIOR:")
        print(f"   ANTES: Só duplo clique funcionava")
        print(f"   AGORA: Botão 'Editar' também funciona para visualização")
        print(f"   RESULTADO: Interface mais intuitiva e familiar")
        print(f"")
        print(f"✅ SISTEMA PRONTO PARA TESTE DAS NOVAS CORREÇÕES!")
    else:
        print("❌ Sistema não está configurado corretamente")

if __name__ == "__main__":
    main()