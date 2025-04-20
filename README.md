# EMAIL-CLASSIFICATION-WITHOUT-UI
This Git hub repository contains the code files related to the assignment task given by akaike company located in Bengaluru. This repository Contains README file which explains you about the code files and how to use this repository.

# SO HOW TO USE THIS EMAIL CLASSIFICATION APP
1. I deployed two versions for email clssification task.
2. One for testing purose and another version is for genral purpose use.
3. Click on this link to view the hugging face space which is specifically designed for testing purpose : https://huggingface.co/spaces/Rohith25Jan/email-classification
   HOW TO USE IT :
   3.1: Click on the link which will you take you to my hugging face space.
   3.2 : You will see blank space after loading. Which looks like this
   ![image](https://github.com/user-attachments/assets/cb23645d-c8a3-4f85-97db-33a888413204)
   3.3 : To test this application, you need to download the tester.py file present in this git hub repo under main branch. Just download it. Open it in vs code or in any other idle.
   ![image](https://github.com/user-attachments/assets/0d5b94c5-6dba-40fc-8bb3-16b8dad7ea40)
   3.4 : you can pass any other email body in any languge, you need to change the content for email_body in tester.py file. Then open terminal run command 'python tester.py' if you are using vs code or you can just run the file.
   3.5 : you can see the response in terminal where the output will be in the format specified in PDF.
   ![image](https://github.com/user-attachments/assets/f0499af5-aab0-4e2f-bbb2-48d1425c4ad0)
   3.6 : WHAT HAPPENED WHEN YOU RUN tester.py
     3.6.1 : actually using request you are sending the input in the json format, A post request as given in the pdf to the hugging space provided at this link : https://huggingface.co/spaces/Rohith25Jan/email-classification. The python files present in the hugging face space will process it and returns the output which will be fetched and displayed in terminal. This is only for testing purpose only.
4. If you want to use this email classification with UI, then click on this link : https://huggingface.co/spaces/Rohith25Jan/email-classification-with-ui
   4.1 : When you click on the lik, it will redirect to my another hugging face space.
   4.2 : Where you will see the interface like this :
   ![image](https://github.com/user-attachments/assets/c76b49c2-2e8f-48f0-856c-a7876a76ce00)
   4.3 : you can see that one drop down menu with two options, like as shown in the below figure
   ![image](https://github.com/user-attachments/assets/bb973526-f90f-400f-8d03-d7fbbfddca95)
   By default the option 1 : Predict with self trained model is selected, that says you are going to implemnet the classification task using the machie learning model which i created from scratch. option 2 says that you are going to perform email classification with an open source llm called laama 3.3-70b-verstaile through Groqh Cloud. so, let's try it with the model which i created. For this you need to give email content and click submit, you will see the output.
   ![image](https://github.com/user-attachments/assets/2563e185-182a-4ba0-856c-c441e1e6db71)
   so you can see that classification is given. You can enter email in ay language like in sanskrit, japanes, chinese etc. I given some email content in sanskrit
   ![image](https://github.com/user-attachments/assets/45327fe8-b2ec-481c-809a-dac586ad86a8)
   So you can give any language, for processing it will be converted into English.
5. About Model Training, Implementation is explained in the Prtoject Report Pdf. Also You can Access Code For
   5.1 : Training ML Model From Scratch : https://colab.research.google.com/drive/12BvbYq5F55lVCjkWSVrBWR1fVsnudSFW?usp=sharing
   5.2 : or else, you can view and download .ipynb file from COLAB FILES FOLDER

6. Tech Stack : Fast API, Pandas, Scikit learn, emoji, langdetect, deep-translator, groq, spacy etc

   




