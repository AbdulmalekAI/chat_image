# %%
from langchain.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
# # %%
# loader=PyPDFLoader("/home/abdulmalek-alsalmi/Desktop/SA/the_project/test/cards.pdf")

# # %%
# cards_pdf = loader.load()
# print(cards_pdf)
# # %%
# len(cards_pdf)
# # %%


# # %%
# r_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=16,
#     chunk_overlap=0, 
#     separators=["\n \n", "\n \n \n", "\n\n", "\n", "\n\n\n", " \n "]
# )

# # %%
# chunks=r_splitter.split_documents(cards_pdf) 
# print('ddddddddddddddd',len(chunks))
# print('the chunks is : ',(chunks))

# # %%
# print(f"len docs is : {len(chunks)}  and len pages is : {len(chunks)} \n\n")

# # %%
from langchain_community.embeddings.ollama import OllamaEmbeddings

# %%
embedding=OllamaEmbeddings(model="nomic-embed-text")
# # %%
from langchain_chroma import Chroma
persist_directory = "/home/abdulmalek-alsalmi/Desktop/SA/the_project/chroma"

# %%
words=[
    "رجل الإطفاء", "رأس", "يستحم", "يأكل", "يتمرن", "يمشي", "يدرس", "يصحو",
    "قفاز", "جورب", "بنطال", "شال", "جزمة", "سفينة", "دراجة نارية", "مروحية",
    "غواصة", "طائرة", "سفينة تجارية", "سفينة فضاء", "جرار", "ثلاجة", "سيارة",
    "غرفة الطعام", "رف", "كرسي", "مرحاض", "مغسلة", "مصباح كهربائي", "بازلاء",
    "بصل", "خيار", "جزر", "فلفل أخضر", "ملفوف", "فجل", "بصر", "طباخ", "الحواس الخمس",
    "دهان", "رسام", "نحات", "قائد أوركسترا", "راعي", "حلاق", "بحار", "طيار", "رائد فضاء", "ممرضة",
    "غسالة", "فرن", "مطبخ", "جارور", "منشفة", "غرفة النوم", "غرفة الحمام", "بندورة", "بطاطا", "الخضروات",
    "باذنجان", "اللمس", "الذوق", "السمع", "الشم", "مغنية", "ممثلة", "خياط", "خباز", "عازف", "صياد",
    "سائق", "باني", "نجار", "السبت", "كهربائي", "الخميس", "الاربعاء", "الجمعة", "الثلاثاء", "الأحد",
    "الإثنين", "أيام الأسبوع", "فراولة", "خروف", "فزاعة", "حصان", "طاحونة", "دجاجة", "بطة", "قش", 
    "قط", "ديك رومي", "محصول", "حضيرة", "أرنب", "ديك", "جرار", "مزارع", "ماعز", "كلب", "بقرة", 
    "صوص", "ثور", "لون أحمر", "لون أبيض", "لون أسود", "لون بنفسجي", "لون زهري", "لون برتقالي",
    "لون أخضر", "لون رمادي", "لون أصفر", "لون بني", "لون أزرق", "رمان", "بطيخ", "أناناس", "أجاص", 
    "مانجو", "عنب", "كرز", "موز", "تفاح", "الفاكهة"
]
# %%
vectordb = Chroma.from_texts(
        texts=words,
        embedding=embedding,
        persist_directory=persist_directory
    )
# %%
# %%
# vectordb._persist_directory("/home/abdulmalek-alsalmi/Desktop/SA/the_project/chroma")
# embedded_query=embedding.embed_query(" ابي ")
# dooo=vectordb.similarity_search_by_vector(embedded_query,k=1)
# %%
print("the result is : ",dooo[0].page_content)
# %%














# # %%
# vectordb = Chroma.from_documents(
#         documents=chunks,
#         embedding=embedding,
#         persist_directory=persist_directory
#     )
# # %%
# print(f"Number of documents in the collection: {vectordb._collection.count()}")# %%

# # %%
# embed_question=embedding.embed_query("النحت على الورق ")
# query="النحت على الورق "
# # %%
# docs = vectordb.similarity_search_by_vector(embed_question,k=1)
# docs[0].page_content

# # %%
# query="المرحاض"
# docs=vectordb.max_marginal_relevance_search(query, k=1, fetch_k=5)
# docs[0].page_content
# # %%

# # %%
# embedded_query = embedding.embed_query("What was the name mentioned in the conversation?")
# embedded_query[:5]
# # %%
# # استخدام طريقة ادخال الكلمات كمصفوفة وتحويلها الى امبيدينج 
# words=[
#     "رجل الإطفاء", "رأس", "يستحم", "يأكل", "يتمرن", "يمشي", "يدرس", "يصحو",
#     "قفاز", "جورب", "بنطال", "شال", "جزمة", "سفينة", "دراجة نارية", "مروحية",
#     "غواصة", "طائرة", "سفينة تجارية", "سفينة فضاء", "جرار", "ثلاجة", "سيارة",
#     "غرفة الطعام", "رف", "كرسي", "مرحاض", "مغسلة", "مصباح كهربائي", "بازلاء",
#     "بصل", "خيار", "جزر", "فلفل أخضر", "ملفوف", "فجل", "بصر", "طباخ", "الحواس الخمس",
#     "دهان", "رسام", "نحات", "قائد أوركسترا", "راعي", "حلاق", "بحار", "طيار", "رائد فضاء", "ممرضة"
# ]
# embeddings = embedding.embed_documents(words)
# len(embeddings), len(embeddings[0])
# # %%
# embedded_query = embedding.embed_query("النحت على الورق ")
# docs=embeddings.similarity_search_by_vector(embedded_query,k=1)
# docs
# %%
#  انشاء قاعدة بينانات نوع كروم من ملف نصي 

#======================================================================================
# %%
from langchain_community.embeddings.ollama import OllamaEmbeddings

# %%
embedding=OllamaEmbeddings(model="nomic-embed-text")
# # %%
from langchain_chroma import Chroma



persist_directory="/home/abdulmalek-alsalmi/Desktop/SA/the_project/chroma"
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)


# %%
# search using by similarity_search
query="  ما هو البطيخ "
result=vectordb.similarity_search(query,k=2)
print('the lenth of result is : ',len(result))
for i in result:
    print(f'the page content id is : {i}')

# # search using by similarity_search_by_vector
# embedded_query=embedding.embed_query(" مصباح  يضيئ في ")
# result=vectordb.similarity_search_by_vector(embedded_query,k=1)
# # %%
# print("the result is : ",result[0].page_content)



# %%
#======================================================================================






#======================================================================================
# Here we load the image from folder images 
# Path of the image is "/home/abdulmalek-alsalmi/Desktop/SA/the_project/images/"
# %%

from PIL import Image
import os
# %%
print(os.path.join("/home/abdulmalek-alsalmi/Desktop/SA/the_project/images/","1.jpg"))

# %% 
def load_image_from_folder(image_name):
    folder_path = "/home/abdulmalek-alsalmi/Desktop/SA/the_project/images/"
    file_path = os.path.join(folder_path, image_name)
    try:
        with Image.open(file_path) as img:
            return img.copy()  # Return a copy of the image to prevent issues after closing
    except (IOError, OSError):
        print(f"Image {image_name} not found or is not a valid image.")
        return None

#======================================================================================
from fpdf import FPDF

# Initialize the PDF
pdf = FPDF()
pdf.add_page()

# Set the path to the Amiri font file
font_path = "/home/abdulmalek-alsalmi/Desktop/SA/the_project/Amiri-1.000/Amiri-Regular.ttf"

# Add the Amiri font
pdf.add_font('ArabicFont', '', font_path, uni=True)
pdf.set_font('ArabicFont', '', 12)

# List of Arabic words
words = [
    "رجل الإطفاء", "رأس", "يستحم", "يأكل", "يتمرن", "يمشي", "يدرس", "يصحو",
    "قفاز", "جورب", "بنطال", "شال", "جزمة", "سفينة", "دراجة نارية", "مروحية",
    "غواصة", "طائرة", "سفينة تجارية", "سفينة فضاء", "جرار", "ثلاجة", "سيارة",
    "غرفة الطعام", "رف", "كرسي", "مرحاض", "مغسلة", "مصباح كهربائي", "بازلاء",
    "بصل", "خيار", "جزر", "فلفل أخضر", "ملفوف", "فجل", "بصر", "طباخ", 
    "الحواس الخمس", "دهان", "رسام", "نحات", "قائد أوركسترا", "راعي", "حلاق",
    "بحار", "طيار", "رائد فضاء", "ممرضة"
]

# Add each word to the PDF
for word in words:
    pdf.cell(0, 10, txt=word, ln=True, align='C')

# Save the PDF file
pdf_file_path = "/home/abdulmalek-alsalmi/Desktop/SA/the_project/cards_one_line.pdf"
pdf.output(pdf_file_path)


##======================================================================================