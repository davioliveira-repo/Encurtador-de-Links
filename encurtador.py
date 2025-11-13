import pyshorteners

def encurtar_url(url_longa):
    """
    Encurta uma URL usando o serviço TinyURL.
    
    Args:
        url_longa (str): A URL original (longa) a ser encurtada.
        
    Returns:
        str: A URL encurtada ou uma mensagem de erro.
    """
    try:
        # Cria uma instância do encurtador. 
        # Aqui, estamos especificando o serviço TinyURL.
        s = pyshorteners.Shortener()
        
        # Chama o método short() do serviço TinyURL
        url_curta = s.tinyurl.short(url_longa)
        
        return url_curta
        
    except pyshorteners.exceptions.ShorteningErrorException as e:
        return f"Erro ao encurtar a URL: O serviço de encurtamento não pôde processar a URL. Detalhes: {e}"
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    print("🚀 Encurtador de Links Simples em Python (TinyURL)")
    print("-" * 45)
    
    # Solicita a URL ao usuário
    url_original = input("🔗 Digite a URL que você deseja encurtar: ")
    
    # Verifica se o usuário inseriu algo
    if url_original:
        print("\n⏳ Encurtando...")
        
        # Chama a função para encurtar
        link_encurtado = encurtar_url(url_original)
        
        # Exibe o resultado
        print("-" * 45)
        print(f"URL Original:  {url_original}")
        print(f"URL Encurtada: {link_encurtado}")
        print("-" * 45)
    else:
        print("\n❌ Nenhuma URL inserida. Programa encerrado.")