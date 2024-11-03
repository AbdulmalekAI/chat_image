# chat_image
# chat_image
requirements :
linux sys 


                                How to run the chat_image project : 
step1: installing ollama and model "nomic-embed-text"
- run the command : : curl -fsSL https://ollama.com/install.sh | sh
## install model "nomic-embed-text"
- run the command : : ollama pull nomic-embed-text

step 2:create a virtual environment
creating the virtual environment
run the command : : python3 -m venv <name_of_virtual_environment>

activating the virtual environment
run the command : : source <name_of_virtual_environment>/bin/activate

step 3 :pull the project from github
go to the project folder and run the command :
run the command :git pull https://github.com/AbdulmalekAI/chat_image.git


step 4 : installing python packages :
run the command : : pip install -r requirements.txt


step5:
- change the path of the database  in the create_db.py 
persist_directory = "/home/abdalmi/Desktop/SA/the_project/chroma" 
persist_directory = "<here is the path of the database>/chroma"

- change the path of the images in the image_loader.py file
image_folder_path = "/home/abdalmi/Desktop/SA/the_project/images/"
image_folder_path = "<here is the path of the images>/images/"

- change of the persistence directory in the main.py file
persist_directory = "/home/abdulmalek-alsalmi/Desktop/SA/the_project/chroma"
persist_directory = "<here is the path of the database>/chroma"

-

change the path of the 



step 6 : run the project:
run the command :
python3 main.py







