from pathlib import Path
import shutil, time, random

class FileClassifier:
    def __init__(self, file_types):
        self.file_types = file_types

    def classify(self, extension):
        self.extension = extension
        for category, extension in self.file_types.items():
            if self.extension in extension:
                return category
        return "Others"

class FileOrganizer():
    def __init__(self, source_folder, classifier):
        self.source_folder = Path(source_folder)
        self.classifier = classifier
        self.history = []

    def organize(self):
        for item in self.source_folder.iterdir():

            if not item.is_file():
                continue
            else:
                category = self.classifier.classify(item.suffix.lower())
                new_folder = self.source_folder / category
                destination = new_folder / item.name 
                new_folder.mkdir(parents=True, exist_ok=True)

                destination = self.get_unique_destination(destination)

                self.history.append({
                    "source": item,
                    "destination": destination
                })

                shutil.move(item, destination)

        return self.history

    def get_unique_destination(self, destination):
        if not destination.exists():
            return destination

        counter = 1

        while True:
            new_destination = destination.parent / (f"{destination.stem}_{counter}{destination.suffix}")
        
            if not new_destination.exists():
                return new_destination

            counter +=1

class FileUndo():
    def undo(self, history):
        for item in history:
            shutil.move(item["destination"], item["source"])

            folder = item["destination"].parent

            if folder.exists() and not any(folder.iterdir()):
                folder.rmdir()

class FileSearcher():
    def __init__(self, source_folder):
        self.source_folder = Path(source_folder)

    def search(self, query):
        results = []
        for i in self.source_folder.rglob("*"):
            if i.is_file() and query.lower() in i.name.lower():
                results.append(i)

        return results



def load_animation():
    random_number = random.randrange(2,7)/100
    for i in range(1, 30):
        print("\r" + "━" * i, end="", flush=True)
        time.sleep(random_number)


def show_menu():
    print("\n" + "=" * 40)
    print("       SMART FILE ORGANIZER")
    print("=" * 40)

    print("\n[1]  Organize Files")
    print("[2]  Search File")
    print("[3]  Exit")


def organize_file(file_types):
    print("\n       ORGANIZE FILES")
    print("-"*40)

    folder_path = Path(input("\nFolder:\n"))
    if folder_path.exists() and folder_path.is_dir():
        history_parent_list = []

        file_classifier = FileClassifier(file_types)
        organizer = FileOrganizer(folder_path, file_classifier)

        print("\n Organizing files...")

        load_animation()

        history = organizer.organize()

        for i in history:
            name = i["destination"].parent.name
            if name not in history_parent_list:
                        history_parent_list.append(name)

        print("\nOrganization completed!\n")
        print(f"Files organized: {len(history)}")
        print(f"Folders created: {len(history_parent_list)}")

        while True:
            undo_or_not = input("\nWant to undo? (Y/N): ").lower()

            if undo_or_not == "y":
                undo_organization(history)
                break
            elif undo_or_not == "n":
                break
            else:
                print("\nEnter valid option (Y/N)")
                
    else:
        print("Invalid path or folder does not exist.")



def search_file():
    print("\n       SEARCH FILE")
    print("-"*40)

    folder_path = Path(input("\nFolder:\n"))
    if folder_path.exists() and folder_path.is_dir():
        
        searcher = FileSearcher(folder_path)

        file_name = input("\nEnter filename to search: ").lower()
        result = searcher.search(file_name)
        print("\nSearching...\n")
        load_animation()

        print("\nSearch Results: \n")

        if result:
            for i in range(0,len(result)):
                print(f"[{i+1}] {result[i].name} -> {result[i]}")

            if len(result)>1:
                print(f"\n{len(result)} results(s) found.\n")
            else: 
                print(f"\n{len(result)} result found.\n")
        else:
            print("\nNo files found.\n")

        input("Press Enter to return to menu...")

    else:
        print("Invalid path or folder does not exist.")

def undo_organization(history):
    print("\n       UNDO ORGANIZATION")
    print("-"*40)

    undo = FileUndo()
    undo.undo(history)

    history_parent_list = []
    history_all_parent_list = []
    history_category_list = []

    for file in history:
        name = file["destination"].parent.name
        history_all_parent_list.append(name)

        if name not in history_parent_list:
            history_parent_list.append(name)

    for i in history_parent_list:
        count = 0
        for j in history_all_parent_list:
            if i == j :
                count +=1
        history_category_list.append({
            i:count
        })

    count_file = len(history)
    count_folder = len(history_parent_list)

    print(f"\n File oraganized: {count_file}")
    print(f"Categories        : {count_folder}\n")

    for n in range(len(history_parent_list)):
        print(f"{history_parent_list[n]:<13} -> {history_category_list[n][history_parent_list[n]]} files")

    print("\nUndoing...\n")
    load_animation()

    print(f"\n{count_file} files restored successfully.")
    print("\nCategory folders removed..\n")

    input("Press Enter to return to menu...")



file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".bmp", ".ico", ".tiff"],

    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt",
        ".xls", ".xlsx", ".csv", ".ppt", ".pptx"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv",
        ".flv", ".webm", ".m4v", ".3gp"
    ],

    "Music": [
        ".mp3", ".wav", ".flac", ".aac",
        ".ogg", ".m4a", ".wma", ".opus"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2", ".xz", ".tar.gz"
    ],

    "Code": [
        ".py", ".js", ".html", ".css", ".java",
        ".c", ".cpp", ".h", ".hpp", ".php",
        ".sql", ".json", ".xml", ".yaml", ".yml",
        ".ts", ".tsx", ".jsx"
    ],

    "Applications": [
        ".exe", ".msi", ".appx", ".apk", ".deb", ".rpm"
    ]
}


def main():

    while True:
        show_menu()
        try:
            choice = input("\nEnter your choice: ")
        except ValueError:
            print("Enter valid option!")
        if choice == "1":
            organize_file(file_types)
        elif choice =="2":
            search_file()
        elif choice =="3":
            print("Thank you for using Smart File Organizer! ")
            print("\nGoodbye\n")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
