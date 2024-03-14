def make_album(artist, album, no_tracks=''):
    """
    A function called make_album() that builds a dictionary
        describing a music album. The function should take in an artist name and an
        album title,
    :return: a dictionary containing these two pieces of information.
    """
    if no_tracks:
        al_bum = {'Artist': artist, 'Album': album, 'Number of Tracks': no_tracks}
    else:
        al_bum = {'Artist': artist, 'Album': album}

    return al_bum


while True:
    print('Enter q to quit')
    input1 = input("Enter Album's Artist name;")
    input2 = input("Enter Album's name;")
    input3 = input("Enter number of tracks on Album")
    if input1 == 'q':
        break
    elif input2 == 'q':
        break
    elif input3 == 'q':
        break

    mine = make_album(input1, input2, input3)
    print(mine)

# a = make_album('Weeknd', 'Starboy')
# b = make_album('Olamide', 'Unruly')
# c = make_album('Post Malone', "Hollywood's Bleeding", 17)
