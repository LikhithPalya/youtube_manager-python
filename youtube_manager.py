import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            content = file.read().strip()
            if not content:
                return []     
            try:       
                data = json.loads(content) #loads data from file(str format) and converts this to json 
                print(f"videos = {data}")
                # print(type(data))
                return data
            except json.JSONDecodeError:
                print("Invalid JSON format in youtube.txt. Resetting to empty list.")
                return []
    except FileNotFoundError:
        return []
    
def save_data_file(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file) # write videos list to file
    

def list_all_videos(videos): #videos are in the format of json
    if not videos:
        print("oops...no videos found.")
        return []
    print('\n')
    print("*" * 70)
    for index, video in enumerate(videos, start=1): #start indexing from 1
        
        print(f"{index}:{video['name']}, Duration: {video['time']}")
    print('\n')
    print("*" * 70)

def add_youtube_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name, 'time':time})
    save_data_file(videos)
    
def update_video_details(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number you want to update"))
    if 1<=index<=len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name':name, 'time':time}
        save_data_file(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("enter the video number to be deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_file(videos)
    else:
        print("Invalid index selected")
    

def main(): 
    videos = load_data()
    while True: #to run the script indefinitely
        print("\n Youtube manager | choose an option")
        print("1. List your favorite videos")
        print("2. add a youtube video")
        print("3. update a youtube video details")
        print("4. delete a youtube video")
        print("5. exit the app")
        
        choice = input("enter your choice = ")
        # print(f"existing videos = {videos}")
        
        match choice :
            case '1':
                print("here is a list of all your favorite videos = ")
                list_all_videos(videos)
            case '2':
                print('add a youtube video to your favorites list')
                add_youtube_video(videos)
            case '3':
                print("update an existing video details")
                list_of_all_videos = list_all_videos(videos)
                update_video_details(videos)
            case '4':
                print("deleting videos")
                delete_video(videos)
                
            case '5':
                print("exit the app")
                break
            
            case _:
                print("invalid option. Select any number between 1&5")

if __name__ == "__main__":
    main()  #if the name of the function is __main__ run the main fn and everything else is a supporting fn