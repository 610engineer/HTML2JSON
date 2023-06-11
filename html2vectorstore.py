from langchain.document_loaders import UnstructuredHTMLLoader

def html_loader(file_path):
    loader = UnstructuredHTMLLoader(file_path)
    #print(loader)
    data = loader.load()
    return data