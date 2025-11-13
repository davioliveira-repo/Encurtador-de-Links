import pyshorteners

def encurtar_url(url_longa):
    try:
        s = pyshorteners.Shortener()
        
        url_curta = s.tinyurl.short(url_longa)
        
        return url_curta
        
    except pyshorteners.exceptions.ShorteningErrorException as e:
        return f"Erro ao encurtar a URL: O serviço de encurtamento não pôde processar a URL. Detalhes: {e}"
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

if __name__ == "__main__":
    print("🚀 Encurtador de Links Simples em Python (TinyURL)")
    print("-" * 45)
    
    url_original = input("🔗 Digite a URL que você deseja encurtar: ")

    if url_original:
        print("\n⏳ Encurtando...")
        
        link_encurtado = encurtar_url(url_original)
        
        print("-" * 45)
        print(f"URL Original:  {url_original}")
        print(f"URL Encurtada: {link_encurtado}")
        print("-" * 45)
    else:
        print("\n❌ Nenhuma URL inserida. Programa encerrado.")
