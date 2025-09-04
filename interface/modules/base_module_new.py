import tkinter as tk
from tkinter import ttk
from utils.theme import PALETTE, FONTS

class BaseModule:
    """Classe base para todos os módulos do sistema com controle de permissões robusto"""
    
    def __init__(self, parent, user_id, role, main_window):
        self.parent = parent
        self.user_id = user_id
        self.role = role
        self.main_window = main_window
        
        # Registrar para receber eventos
        if hasattr(main_window, 'register_listener'):
            main_window.register_listener(self.handle_event)
        
        # Frame principal do módulo (container visual)
        self.frame = tk.Frame(parent, bg=PALETTE["bg_app"])
        self.frame.pack(fill="both", expand=True)
        
        # Configurar UI específica do módulo
        self.setup_ui()
        
        # Aplicar modo somente leitura automaticamente baseado nas permissões
        self._apply_permissions_automatically()
    
    def _apply_permissions_automatically(self):
        """Aplica automaticamente as permissões baseado no nível de acesso do usuário"""
        if not hasattr(self.main_window, 'can_edit'):
            return
            
        # Determinar qual módulo este é baseado no nome da classe
        module_key = self.__class__.__name__.lower().replace('module', '')
        
        # Se o usuário não pode editar, aplicar modo somente leitura
        if not self.main_window.can_edit(module_key):
            self.set_read_only(True)
            print(f"🔒 Módulo {module_key} configurado como somente leitura para usuário {self.user_id}")
        
    def setup_ui(self):
        """Método a ser implementado pelos módulos filhos"""
        pass
        
    def handle_event(self, event_type, data=None):
        """Manipular eventos recebidos do sistema"""
        pass
        
    def emit_event(self, event_type, data=None):
        """Emitir evento para outros módulos"""
        if hasattr(self.main_window, 'emit_event'):
            self.main_window.emit_event(event_type, data)
    
    def has_role(self, role_name: str) -> bool:
        """Verifica se o usuário possui o perfil informado (suporta múltiplos perfis separados por vírgula)."""
        try:
            roles = [r.strip().lower() for r in (self.role or '').split(',') if r.strip()]
            return role_name.lower() in roles
        except Exception:
            return self.role == role_name
    
    def can_edit(self, module_key: str = None) -> bool:
        """Verifica se o usuário pode editar o módulo atual"""
        if self.has_role('admin'):
            return True
        
        if not hasattr(self.main_window, 'can_edit'):
            return True
            
        # Se não especificar módulo, tentar inferir do nome da classe
        if module_key is None:
            module_key = self.__class__.__name__.lower().replace('module', '')
            
        return self.main_window.can_edit(module_key)
    
    def can_add(self, module_key: str = None) -> bool:
        """Verifica se o usuário pode adicionar itens no módulo atual"""
        return self.can_edit(module_key)
    
    def can_delete(self, module_key: str = None) -> bool:
        """Verifica se o usuário pode deletar itens no módulo atual"""
        return self.can_edit(module_key)
    
    def set_read_only(self, read_only: bool = True):
        """Define o módulo como somente leitura"""
        self.read_only = read_only
        self._apply_read_only_state()
    
    def _apply_read_only_state(self):
        """Aplica o estado de somente leitura aos widgets"""
        if not hasattr(self, 'read_only') or not self.read_only:
            return
            
        # Desabilitar todos os campos de entrada
        for widget in self.frame.winfo_children():
            self._disable_widget_recursive(widget)
    
    def _disable_widget_recursive(self, widget):
        """Desabilita um widget e seus filhos recursivamente"""
        try:
            # Desabilitar widgets de entrada
            if isinstance(widget, (tk.Entry, tk.Text, tk.Spinbox)):
                widget.config(state='disabled')
            elif isinstance(widget, ttk.Entry):
                widget.config(state='disabled')
            elif isinstance(widget, (tk.Checkbutton, tk.Radiobutton)):
                widget.config(state='disabled')
            elif isinstance(widget, ttk.Combobox):
                widget.config(state='disabled')
            elif isinstance(widget, tk.Button):
                # Manter botões de consulta habilitados, desabilitar os de edição
                if any(keyword in widget.cget('text').lower() for keyword in ['editar', 'adicionar', 'remover', 'excluir', 'salvar', 'novo', 'criar', 'modificar', 'atualizar']):
                    widget.config(state='disabled')
            
            # Processar filhos recursivamente
            for child in widget.winfo_children():
                self._disable_widget_recursive(child)
        except Exception:
            pass
    
    def create_section_frame(self, parent, title, padx=10, pady=10):
        """Criar frame de seção com título (compatível com uso anterior).

        Retorna um Frame que o chamador pode `pack` normalmente e adicionar
        widgets filhos dentro. O próprio frame já contém um cabeçalho e
        área de conteúdo, mas para manter compatibilidade, o conteúdo
        também pode ser adicionado diretamente no frame retornado.
        """
        container = tk.Frame(parent, bg='#ffffff', highlightthickness=1, highlightbackground=PALETTE["border"]) 
        # Header
        header = tk.Label(container, text=title, font=FONTS["subtitle"], bg='#ffffff', fg=PALETTE["text_primary"])
        header.pack(anchor="w", padx=12, pady=(12, 6))
        # Inner content holder (optional use)
        content = tk.Frame(container, bg='#ffffff')
        content.pack(fill="both", expand=True, padx=12, pady=(0, 12))
        # For backward compatibility, allow adding directly to container
        container.content = content
        return container
    
    def create_button(self, parent, text, command, variant='primary', **kwargs):
        """Criar botão estilizado (mantém assinatura compatível por kwargs).
        Remove opções não suportadas por ttk.Button (ex.: bg, fg, relief...).
        """
        style = {
            'primary': 'Secondary.TButton',
            'success': 'Secondary.TButton',
            'danger': 'Secondary.TButton',
            'secondary': 'Secondary.TButton',
            'ghost': 'Secondary.TButton',
        }.get(variant, 'Secondary.TButton')

        # Sanitize unsupported ttk options passed from legacy calls
        unsupported = {
            'bg', 'background', 'fg', 'foreground', 'relief', 'bd', 'borderwidth',
            'highlightthickness', 'cursor', 'padx', 'pady'
        }
        safe_kwargs = {k: v for k, v in kwargs.items() if k not in unsupported}

        button = ttk.Button(parent, text=text, command=command, style=style, **safe_kwargs)
        return button
    
    def create_search_frame(self, parent, placeholder="Buscar...", command=None):
        """Criar frame de busca padronizado"""
        search_frame = tk.Frame(parent, bg='#ffffff', highlightthickness=1, highlightbackground=PALETTE["border"]) 
        
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var)
        search_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=(8, 0), pady=6)
        search_entry.insert(0, placeholder)

        def _on_focus_in(_e):
            if search_entry.get() == placeholder:
                search_entry.delete(0, 'end')
        def _on_focus_out(_e):
            if not search_entry.get().strip():
                search_entry.insert(0, placeholder)
        search_entry.bind('<FocusIn>', _on_focus_in)
        search_entry.bind('<FocusOut>', _on_focus_out)
        
        if command:
            search_btn = self.create_button(search_frame, "Buscar", command, variant='primary')
            search_btn.pack(side="right", padx=8, pady=6)
            search_entry.bind('<Return>', lambda e: command())
        
        return search_frame, search_var
    
    def show_success(self, message):
        """Mostrar mensagem de sucesso"""
        from tkinter import messagebox
        messagebox.showinfo("Sucesso", message)
        
    def show_error(self, message):
        """Mostrar mensagem de erro"""
        from tkinter import messagebox
        messagebox.showerror("Erro", message)
        
    def show_warning(self, message):
        """Mostrar mensagem de aviso"""
        from tkinter import messagebox
        messagebox.showwarning("Aviso", message)
        
    def show_info(self, title, message):
        """Mostrar mensagem informativa"""
        from tkinter import messagebox
        messagebox.showinfo(title, message)
