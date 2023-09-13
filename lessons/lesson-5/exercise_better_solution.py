story_file = open("files/sample-1.txt", "r")

story_lines = int(input("Mitu rida juttu tahad? "))

for i in range(story_lines):
    print(story_file.readline())