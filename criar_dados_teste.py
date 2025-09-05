#!/usr/bin/env python3
"""
Script para criar dados de teste no sistema
"""

import sqlite3
from database import DB_NAME, criar_banco

def criar_dados_teste():
    """Criar alguns clientes e produtos de teste"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    try:
        # Verificar se já existem dados
        c.execute("SELECT COUNT(*) FROM clientes")
        clientes_count = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM produtos")
        produtos_count = c.fetchone()[0]
        
        print(f"📊 Dados existentes: {clientes_count} clientes, {produtos_count} produtos")
        
        # Criar clientes de teste se não existirem
        if clientes_count == 0:
            clientes_teste = [
                ("Empresa ABC Ltda", "ABC Compressores", "12.345.678/0001-90", "Rua das Flores, 123", "São Paulo", "SP", "01234-567", "(11) 99999-1234", "contato@abc.com"),
                ("Indústria XYZ S/A", "XYZ Industrial", "98.765.432/0001-10", "Av. Industrial, 456", "Rio de Janeiro", "RJ", "20123-456", "(21) 88888-5678", "vendas@xyz.com"),
                ("Companhia DEF", "DEF Máquinas", "11.222.333/0001-44", "Rua da Tecnologia, 789", "Belo Horizonte", "MG", "30456-789", "(31) 77777-9012", "info@def.com")
            ]
            
            for nome, nome_fantasia, cnpj, endereco, cidade, estado, cep, telefone, email in clientes_teste:
                c.execute("""
                    INSERT INTO clientes (nome, nome_fantasia, cnpj, endereco, cidade, estado, cep, telefone, email)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (nome, nome_fantasia, cnpj, endereco, cidade, estado, cep, telefone, email))
                
            print("✅ Clientes de teste criados")
        
        # Criar produtos de teste se não existirem
        if produtos_count == 0:
            produtos_teste = [
                ("Compressor de Ar 10HP", "Produto", "84141000", 2500.00, "Compressor de ar industrial 10HP com tanque de 200L", 1),
                ("Manutenção Preventiva", "Serviço", "", 350.00, "Serviço de manutenção preventiva completa", 1),
                ("Filtro de Ar Industrial", "Produto", "84219900", 85.50, "Filtro de ar para compressores industriais", 1),
                ("Instalação de Compressor", "Serviço", "", 450.00, "Serviço de instalação e configuração de compressor", 1),
                ("Kit de Vedação", "Produto", "40169300", 125.00, "Kit completo de vedação para compressores", 1)
            ]
            
            for nome, tipo, ncm, valor, descricao, ativo in produtos_teste:
                c.execute("""
                    INSERT INTO produtos (nome, tipo, ncm, valor_unitario, descricao, ativo)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (nome, tipo, ncm, valor, descricao, ativo))
                
            print("✅ Produtos de teste criados")
        
        # Criar alguns contatos para os clientes
        c.execute("SELECT id FROM clientes LIMIT 3")
        clientes_ids = [row[0] for row in c.fetchall()]
        
        for cliente_id in clientes_ids:
            # Verificar se já tem contatos
            c.execute("SELECT COUNT(*) FROM contatos WHERE cliente_id = ?", (cliente_id,))
            if c.fetchone()[0] == 0:
                c.execute("""
                    INSERT INTO contatos (cliente_id, nome, cargo, telefone, email)
                    VALUES (?, ?, ?, ?, ?)
                """, (cliente_id, "João Silva", "Gerente de Compras", "(11) 99999-0001", "joao@empresa.com"))
                
        print("✅ Contatos de teste criados")
        
        conn.commit()
        
        # Mostrar estatísticas finais
        c.execute("SELECT COUNT(*) FROM clientes")
        clientes_final = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM produtos")
        produtos_final = c.fetchone()[0]
        
        c.execute("SELECT COUNT(*) FROM contatos")
        contatos_final = c.fetchone()[0]
        
        print(f"\n📊 DADOS FINAIS:")
        print(f"   • {clientes_final} clientes")
        print(f"   • {produtos_final} produtos/serviços")
        print(f"   • {contatos_final} contatos")
        
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Erro ao criar dados de teste: {e}")
        return False
    finally:
        conn.close()

def main():
    print("=== CRIAÇÃO DE DADOS DE TESTE ===\n")
    
    # Garantir que o banco existe
    criar_banco()
    print("✅ Banco de dados verificado\n")
    
    # Criar dados de teste
    if criar_dados_teste():
        print(f"\n✅ Dados de teste criados com sucesso!")
        print(f"\n🧪 Agora você pode testar o sistema:")
        print(f"   1. Execute: python3 main.py")
        print(f"   2. Login: teste_consulta / 123456")
        print(f"   3. Teste duplo clique nos módulos Clientes e Cadastros")
    else:
        print("❌ Falha ao criar dados de teste")

if __name__ == "__main__":
    main()