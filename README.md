# EMAIL CLASSIFICATION SYSTEM
![image](https://github.com/user-attachments/assets/550d2104-f3b4-42ca-8d25-30a763b04b18)
# STEP BY STEP DETAILED GUIDE
### HOW THIS REPOSITORY IS STRUCTURED
1. This Repository contains 5 folders, one .txt file and two nested directories.
2. Which are : Colab Note Books, Datasets, Documents, Models & Python Files.
3. **Colab Note Books** : Contians .ipynb, .py, pdf version of .ipynb files which displays the code used to train the ML Model for email classification from scartch.
4. **Data sets** : Contains Datasets that includes dataset provided in pdf, datasets that are saved during the process of training models.
5. **Models** : Contains .pkl files & .txt file. .txt file contains links which allows you to download the actual .pkl models that are used in this application.
6. **Python Files** : Contains api.py, app.py, models.py, utils.py files as described in the pdf. But those files are present in two directories which are present inside the Python Files directory. Both these directories conteins the above mentioned .py files. You can assume these two directories are like two versions for the current project.
7. **requirements.txt** : contains the list of python packages and libraries used for this purpose.
8. **deploymentLinks.txt** : contains links, which redirects you to the deployed and ready to use web site for this project called **Email Classification System For Support Team**

# STEP BY STEP GUIDE ON HOW TO USE THIS PROJECT
![image](https://github.com/user-attachments/assets/a7c9ce4b-4da0-4d5f-87a9-14280984347a)
This project comes with two versions which are known as
1. Tester version
2. User version

Tester version is used for assessing the quality of this project through the system or any automated grading system. Whereas user version comes with a web site application with front end, so that user can use this web application.

**You can access any version with the below given links :**
Tester Version : <version link>
User version : <version link>

I used hugging face Spaces as a deployment platform with docker image.

# STEP BY STEP GUIDE ON HOW TO USE TESTER VERSION
1. Note : Use this link (https://huggingface.co/spaces/Rohith25Jan/email-classification) to go the tester version.
2. Actually, tester version is made for assessing the quality of project and validating output structure mantioned in the pdf.
3. So, when you redirected to the web site, you may not see any thing except one blank web page which is in Running State.
4. So, you no need to visit the website if you want to test this project.
5. But, to test the project you need to download the tester.py file present in Python Files Directory ---> Email Classifier For Testing ---> tester.py
6. After downloading the tester.py, open it using any code editor or IDLE. I used vs code. You can see the image for refernce
7. ![image](https://github.com/user-attachments/assets/6597d0e5-6d16-4ebb-83b8-f2cdafb317ff)
8. So, You can keep the code as it is, i will explain the code in short. The code uses request model and it sends a POST request to the **Tester version** website, which is made using FastAPI. So, all the processing will be done using the .py files present in **Python Files Directory/Email Classifier For Testing**. Returns a json object. which will be fetched using request.response. If successfull you will get 200 server response.
9. If you want to send your email_body, just change the value for the key calld 'email_body' in test_email dictionery. Refer the below image.
10. ![image](https://github.com/user-attachments/assets/eace53af-7b32-4c92-aac0-d45031374802)
11. You can give email_body in **any language** but you have to give it as a string datatype which may be single line or multi line string.
12. The output for the above email_body is shown below
13. ![image](https://github.com/user-attachments/assets/66491795-6cb7-423b-80e5-ab36e2db7c5a)
14. As You can see the out put is obtained but it is the dictionery form. So to visualize the out put in a pretiest way and to use the application with front end, you can use User Version.

# STEP BY STEP GUIDE ON HOW TO USE USER VERSION
1. go to the website : https://huggingface.co/spaces/Rohith25Jan/email-classification-with-ui
2. you will see the user interface like shown in the below figure
3. ![image](https://github.com/user-attachments/assets/16cc43e2-4a36-4260-9d81-98335dba9af0)
4. You can see one drop down, one text area and one submit button.
5. So, you can classify the emails in two approaches. one is using self trained ML model trained by me and you can download those models in Models Directory through the link files given. Another approach is using a populer open source llm called 'laama 3.3-70b-versatile' through Groq cloud.
6. If you want to classify emails using LLM, then you need an API key which is absolutely free to call model. You can get that API from Groq Cloud which is one the fastest AI Inference.
7. So, let's classify the email using self trained ML Model.
8. I passed email in the teaxt area specified, and then clicked submit. so output is obtained, which is shown in below figure.
9. I given the email content in sanskrit language then we got the classification which is shown in the below image
10. ![image](https://github.com/user-attachments/assets/f981ed66-893b-4885-8f66-239801e79263)
11. This time given content in telugu got the result, shown in the below image
12. ![image](https://github.com/user-attachments/assets/e79e1bf9-84fe-4ab6-b686-bb8ca36873d1)
13. This time given content in hindi, got output , shown in the below image
14. ![image](https://github.com/user-attachments/assets/34fe5d06-bac1-4eac-bb29-179c3bb44dfa)
15. This time given content in japanese, got output, which is shown in the below image
16. ![image](https://github.com/user-attachments/assets/87b69458-e206-4436-be86-d205ed85e150)
17. You can give any language, at backend language translation to english will be done for implenting robust email classification

# STEP BY STEP EXPLANATION ON IMPLEMENTATION FOR THIS PROJECT







