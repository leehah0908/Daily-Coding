def solution(genre_array, play_array):
    genre = set(genre_array)
    val_dict = {}
    result = []
    
    for i in genre:
        val_dict[i] = 0

    for i in range(len(genre_array)):
        val_dict[genre_array[i]] += play_array[i]
    
    sorted_dict = dict(sorted(val_dict.items(), key=lambda x : x[1], reverse=True))
    
    for i in sorted_dict.keys():
        temp_genre = {}
        for j in range(len(genre_array)):
            if genre_array[j] == i:
                temp_genre[j] = play_array[j]

        sorted_genre = dict(sorted(temp_genre.items(), key=lambda x : x[1], reverse=True))
        count = 0
        for k in sorted_genre:
            if count == 2:
                break
            result.append(k)
            count += 1
    return result