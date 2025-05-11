# 🎬 YouTube Video Manager (Python CLI App)

A simple command-line application to manage your favorite YouTube videos using Python. This tool allows you to **add**, **list**, **update**, and **delete** videos with persistent storage using a local JSON file.

---

## 📂 Project Structure

* `youtube_manager.py` – Main CLI application
* `youtube.txt` – Data file storing video info in JSON format

---

## 🚀 Features

* ✅ List all your saved YouTube videos
* ➕ Add a new video with name and duration
* 🛠️ Update existing video details
* ❌ Delete a video by number
* 💾 Automatically saves changes to `youtube.txt`

---

## 📦 Requirements

* Python 3.7 or higher
  (No external libraries needed — uses only built-in Python modules.)

---

## 🧑‍💻 How to Run

1. **Clone the repository:**

   `git clone https://github.com/yourusername/youtube-manager.git`
   `cd youtube-manager`

2. **Run the script:**

   `python3 youtube_manager.py`

3. **Use the menu:**

   ```
   Youtube manager | choose an option
   1. List your favorite videos
   2. Add a YouTube video
   3. Update a YouTube video details
   4. Delete a YouTube video
   5. Exit the app
   ```

---

## 📝 Example Data in `youtube.txt`

```json
[
  {
    "name": "Python Tutorial for Beginners",
    "time": "10:34"
  },
  {
    "name": "How to Use Git",
    "time": "8:45"
  }
]
```

---

## 🛡️ Error Handling

* Gracefully handles missing or empty `youtube.txt`
* Skips corrupted JSON files and resets to an empty list
* Validates video selection when updating or deleting

---

## 📌 To-Do

* [ ] Add search functionality
* [ ] Add categories/tags
* [ ] Export/import to CSV
* [ ] Create a GUI using Tkinter or PyQt

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).


