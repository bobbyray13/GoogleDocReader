import os
import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def main():
    # authenticate and build the drive and docs services
    credentials_path = (r"C:\Users\Bobby\Documents\Programming\jsonfiles\FRB2b.json")
    credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=["https://www.googleapis.com/auth/drive"])
    drive_service = build("drive", "v3", credentials=credentials)
    docs_service = build("docs", "v1", credentials=credentials)

    # prompt the user to select an option
    user_choice = input("What would you like to view today? [Speeches, Articles, Editorials]: ")
    if user_choice.lower() == "speeches":
        view_speeches(drive_service, docs_service)
    elif user_choice.lower() == "articles":
        view_articles(drive_service, docs_service)
    elif user_choice.lower() == "editorials":
        view_editorials(drive_service, docs_service)
    else:
        print("Invalid option. Please choose from [Speeches, Articles, Editorials]")

from googleapiclient.errors import HttpError


def view_speeches(drive_service, docs_service):
    # get a list of files in the speeches folder
    folder_id = "1fdVSWc82IO4sR04EjXNc3HPUxi1gD3Mb" # replace with the ID of your speeches folder
    query = "mimeType='application/vnd.google-apps.document' and trashed=false and '{}' in parents".format(folder_id)
    try:
        results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
        items = results.get("files", [])
        if not items:
            print("No files found in the speeches folder")
        else:
            # display the list of files
            print("Speeches in the folder:")
            for item in items:
                print(item["name"])

            # prompt the user to enter a file name
            file_name = input("Enter the name of a speech to display its contents: ")
            # search for the file in the speeches folder
            query = "name='{}' and mimeType='application/vnd.google-apps.document' and trashed=false and '{}' in parents".format(file_name, folder_id)
            results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
            items = results.get("files", [])
            if not items:
                print("Speech not found")
            else:
                # get the ID of the first matching file
                file_id = items[0]["id"]
                print("Speech found with ID: ", file_id)

                # retrieve the text content of the file using the docs API
                doc = docs_service.documents().get(documentId=file_id).execute()
                doc_content = doc.get("body").get("content")
                text = ""
                for elem in doc_content:
                    if "paragraph" in elem:
                        elements = elem.get("paragraph").get("elements")
                        for run in elements:
                            if "textRun" in run:
                                text += run.get("textRun").get("content")

                # print the content of the file
                print(text)
    except HttpError as error:
        print("An error occurred: {}".format(error))

def view_articles(drive_service, docs_service):
    # get a list of files in the speeches folder
    folder_id = "1yCil9M9qS6LiqyWVOSvDudvgnv-eVaQ3"
    query = "mimeType='application/vnd.google-apps.document' and trashed=false and '{}' in parents".format(folder_id)
    try:
        results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
        items = results.get("files", [])
        if not items:
            print("No files found in the speeches folder")
        else:
            # display the list of files
            print("Speeches in the folder:")
            for item in items:
                print(item["name"])

            # prompt the user to enter a file name
            file_name = input("Enter the name of a speech to display its contents: ")
            # search for the file in the speeches folder
            query = "name='{}' and mimeType='application/vnd.google-apps.document' and trashed=false and '{}' in parents".format(file_name, folder_id)
            results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
            items = results.get("files", [])
            if not items:
                print("Speech not found")
            else:
                # get the ID of the first matching file
                file_id = items[0]["id"]
                print("Speech found with ID: ", file_id)

                # retrieve the text content of the file using the docs API
                doc = docs_service.documents().get(documentId=file_id).execute()
                doc_content = doc.get("body").get("content")
                text = ""
                for elem in doc_content:
                    if "paragraph" in elem:
                        elements = elem.get("paragraph").get("elements")
                        for run in elements:
                            if "textRun" in run:
                                text += run.get("textRun").get("content")

                # print the content of the file
                print(text)
    except HttpError as error:
        print("An error occurred: {}".format(error))

def view_editorials(drive_service, docs_service):
    # get a list of files in the speeches folder
    folder_id = "1Gnmq8kndTsI0DQULe2fFSGFMdrjAGPi1"
    query = "mimeType='application/vnd.google-apps.document' and trashed=false and '{}' in parents".format(folder_id)
    try:
        results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
        items = results.get("files", [])
        if not items:
            print("No files found in the speeches folder")
        else:
            # display the list of files
            print("Speeches in the folder:")
            for item in items:
                print(item["name"])

            # prompt the user to enter a file name
            file_name = input("Enter the name of a speech to display its contents: ")
            # search for the file in the speeches folder
            query = "name='{}' and mimeType='application/vnd.google-apps.document' and trashed=false and '{}' in parents".format(file_name, folder_id)
            results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
            items = results.get("files", [])
            if not items:
                print("Speech not found")
            else:
                # get the ID of the first matching file
                file_id = items[0]["id"]
                print("Speech found with ID: ", file_id)

                # retrieve the text content of the file using the docs API
                doc = docs_service.documents().get(documentId=file_id).execute()
                doc_content = doc.get("body").get("content")
                text = ""
                for elem in doc_content:
                    if "paragraph" in elem:
                        elements = elem.get("paragraph").get("elements")
                        for run in elements:
                            if "textRun" in run:
                                text += run.get("textRun").get("content")

                # print the content of the file
                print(text)
    except HttpError as error:
        print("An error occurred: {}".format(error))

if __name__ == '__main__':
    main()
