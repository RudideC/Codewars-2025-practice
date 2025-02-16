count = input()

songs = []
for i in range(int(count)):
    songs.append(input())

while len(songs) > 0:
    count = 0
    first_song = songs[0].strip()
    for i in range(len(songs)):
        if songs[i - count].strip() == first_song:
            songs.pop(i - count)
            count += 1
    print(f"{count} {first_song}")