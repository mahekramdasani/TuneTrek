import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "music.settings")
django.setup()
import json
from musicrecommend.models import Song
# from api.models import UserLike,CustomUser  # Import the UserLike model
from django.contrib.auth.models import User  # Import the User model
import random

def load_data_from_json():
    # Create a temporary user for data import
    # import_user, created = User.objects.get_or_create(username='import_user')

    with open('C:\\Users\\Lenovo\\Mini Project\\songs.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        random.shuffle(data)

        for record in data:
            # Create the Song instance
            song= Song.objects.create(
            song_id = record['id'],
            title =  record['song'],
            artist= record['artist'],
            lyrics= record['lyrics'],
            image_url= record['img']
                # Add other fields as needed
        )

            # Create a UserLike instance and associate it with the import_user and song
#             admin_user,created = CustomUser.objects.get_or_create(first_name='admin')

# # Create a UserLike instance for the admin user and associate it with the song
#             user_like = UserLike.objects.create(user=admin_user, song=song)

if __name__ == '__main__':
    load_data_from_json()
