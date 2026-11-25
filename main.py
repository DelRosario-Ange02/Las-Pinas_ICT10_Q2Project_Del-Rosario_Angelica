
from pyscript import document
from js import window

def candidate_checker(e):

    club_members = [
        "ange del rosario",
        "lexie uaje",
        "ranee de guzman",
        "lan rome aguilar",
        "tony salonga"
    ]

    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()

    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members

    if member_checker:
        document.getElementById('result').innerHTML = (
            f'Congratulations {candidate}, you are now part of Marching Band!'
        )

        window.location.href = "mainpage.html"

    else:
        document.getElementById('result').innerHTML = (
            f'Sorry {candidate}, your name is not on the list.'
        )


from pyscript import document

instruments = {
    "Snare Drum": ("Sticks", "Provides rhythms and rudiments"),
    "Tenor Drums": ("Mallets", "Plays melodic patterns and transitions"),
    "Bass Drum": ("Bass Drum Mallets", "Provides low rhythmic foundations"),
    "Cymbals": ("Cymbal-to-cymbal technique", "Provides accents and crashes"),
    "Vibraphone": ("Mallets", "Produces sustained, shimmering tones"),
    "Glockenspiel": ("Hard Mallets", "Produces high-pitched, bell-like tones"),
    "Tambourine": ("Hand or Stick", "Adds jingling rhythmic accents"),
    "Maracas": ("Shaking", "Provides rattling rhythmic patterns and accents"),
}

def instrument_info(event=None):

    instrument = document.getElementById("elementInput").value.strip().title()

    instrument_data = instruments.get(
        instrument, ("-", "Instrument not found")
    )

    document.getElementById("result").innerHTML = f"""
        <b>Instrument:</b> {instrument if instrument in instruments else "Instrument not found"}<br>
        <b>Playing Technique:</b> {instrument_data[0]}<br>
        <b>Role:</b> {instrument_data[1] if instrument in instruments else "-"}
    """
