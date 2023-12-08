import pandas as pd
import os
import re
import gdown
from PIL import Image, ImageFilter
def download_member_csv():
    print("Downloading member information from Google Sheets")
    file_url ="https://docs.google.com/spreadsheets/d/1pecx-Dt7CR7h5_yngS_Wwr-i5ONi_HOeiaVnb_A1L5E/edit?usp=sharing"
    gsheetkey = "1pecx-Dt7CR7h5_yngS_Wwr-i5ONi_HOeiaVnb_A1L5E"
    sheet_name = 'member-information'
    url=f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
    df = pd.read_excel(url,sheet_name=sheet_name)
   
    current_dir = os.getcwd()
    output_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    output_dir = os.path.join(current_dir, 'raw_data')
    os.makedirs(output_dir, exist_ok=True)
    raw_csv_file = os.path.join(output_dir, 'afretec-member-information.csv')
    print(f"Saving raw member information to {raw_csv_file}")
    df.to_csv(raw_csv_file, index=False)
def add_image_file_name(df):
    df['Image'] = df.apply(lambda row: get_image_file_name(row), axis=1)
    del df['Photo']
    return df
def download_images(df):
    root_path = os.path.join(os.path.dirname(__file__),
                                 '../assets/img/members/raw')
    os.makedirs(root_path, exist_ok=True)
    
    for _, row in df.iterrows():
        photo = row['Photo']
        image_url = construct_image_url(photo)
        if image_url is None:
            continue
        file_name =f"{row['FirstName']}_{row['LastName']}.jpg"
        out_file = os.path.join(root_path, file_name)
        #print(f"Downloading {image_url} to {out_file}")
        gdown.download(image_url, out_file, quiet=False)

def get_image_file_name(row):
    file_name = None 
    if len(str(row['Photo'])) < 10:
        if row['Gender'] == "Male":
            file_name = "male-person.jpg"
        else:
            file_name = "female-person.jpg"
    else: 
        file_name =f"{row['FirstName']}_{row['LastName']}.jpg".replace(" ", "")
    return file_name
    
def construct_image_url(url):
    image_id = extract_drive_id(url)
    if image_id is None:
        return None
    return f"https://drive.google.com/uc?export=view&id={image_id}"      
def rename_columns(df):
    print("Deleting the timestamp column")
    del df['Timestamp']
    columns_dict ={
        'What is your preferred title ?': 'Title',
        'First Name': 'FirstName', 
        'Last Name': 'LastName', 
        'What is your gender?': 'Gender',
        'Email': 'Email', 
        'What is the name of your institution or university?': 'Institution',
        'What is the country of your university affiliation?': 'Country',
        'What are your primary research interests or areas of expertise? (Select all that apply)': 'Expertises',
        'What is your current occupation or professional role? Please select the category that best describes your primary role.': 'Occupation',
        'Would you be interested in leading the AFRETEC Health Sub-Cluster at your institution?': 'SubclusterLeader',
        'What is the URL link for your Google Scholar account?': 'GoogleScholar',
        'What is the URL link for your ORCID  account?': 'ORCID',
        'What is the URL link for your LinkedIn account?': 'LinkedIn',
        'Do you have a personal website? If so, what is the link to your personal website?': 'Website',
        'Would you like to include a photo of yourself on the research website? If yes, please upload a professional photo that you would like to be used': 'Photo'}
    print("Renaming columns")
    df.rename(columns=columns_dict, inplace=True)
    df['Photo'] = df['Photo'].apply(construct_image_url)
    return df

def clean_member_info():
    current_dir = os.path.dirname(__file__)
    raw_csv_file = os.path.join(current_dir, '../raw_data/afretec-member-information.csv')
    df = pd.read_csv(raw_csv_file)
    df = rename_columns(df)
    df=add_image_file_name(df)
    df['Website'] = df['Website'].apply(clean_member_website)
    renamed_csv_file = os.path.join(current_dir,
                                    '../_data/members.csv')
    print(f"Saving renamed DataFrame to {renamed_csv_file}")
    df.to_csv(renamed_csv_file, index=False)

    # Delete the raw CSV file
    #print("Deleting the raw CSV file")
    #os.remove(raw_csv_file)
    return df 
def clean_member_website(row):
    #check if the row is a websie or not
    if not str(row).startswith("http"):
        return ""
    else:
        return row
def extract_drive_id(url):
    if len(str(url)) <10:
        return None
    pattern = r'(?<=id=)[a-zA-Z0-9_-]+'
    match = re.search(pattern, url)
    return match.group() if match else None
def resize_and_compress_images(quality=85):
    # Create the output directory if it doesn't exist
    input_dir =os.path.join(os.path.dirname(__file__),
                                 '../assets/img/members/raw')
    output_dir =os.path.join(os.path.dirname(__file__),
                                 '../assets/img/members/resized')
    os.makedirs(output_dir, exist_ok=True)

    # Loop through each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            # Construct the full file paths
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            # Open the image
            with Image.open(input_path) as img:
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                mywidth = 600
                wpercent = (mywidth/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                
                # Resize the image to the target size
                resized_img = img.resize((mywidth,hsize), resample=Image.LANCZOS)

                # Save the resized and compressed image
                resized_img.save(output_path, optimize=True, quality=quality)

                

if __name__ == '__main__':
    #download_member_csv()
    df = clean_member_info()
    #download_images(df)
    #resize_and_compress_images()
    
   
   
    
    

    
  

