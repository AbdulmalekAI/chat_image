# %%
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_chroma import Chroma
# %%
embedding=OllamaEmbeddings(model="nomic-embed-text")
persist_directory="/home/abdulmalek-alsalmi/Desktop/SA/the_project/chroma"
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

query="ldjf sdfsd sdf;"
# %%
# البحث عن التشابة مع اعادة رقم التشابه
result=vectordb.similarity_search_with_score(query=query, k=1)
for res, score in result:
    print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")
# %%
# استخدام طريقة البحث باستخدام الفكتور
result=vectordb.similarity_search_by_vector(embedding=embedding.embed_query(query), k=2)  
print(result)
# print(result['original_text'])

# %% 
# البحث باستخدام mmr
retriever = vectordb.as_retriever(
    search_type="mmr", search_kwargs={"k": 1, "fetch_k": 5,"lambda_mult": 0.1}
)
retriever.invoke(query)
# # %%
# result=vectordb.max_marginal_relevance_search(query=query, "k": 1, "fetch_k": 5,"lambda_mult": 0.1)   
# print(result)


# %%
def search_by_similarity(query, vectordb):
    result = vectordb.similarity_search(query, k=1)
    return result[0].page_content

def init_vectordb():
    embedding = OllamaEmbeddings(model="nomic-embed-text")
    persist_directory = "/home/abdulmalek-alsalmi/Desktop/SA/the_project/chroma"
    return Chroma(persist_directory=persist_directory, embedding_function=embedding)
# %%
print(vectordb._collection.count())
# %%
