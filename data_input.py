from commander import Commander
import constants

def commanders():
	commander_list = []

	colors = []
	#https://archidekt.com/decks/3255717 Baru, Wurmspeaker           Green
	name = 'Baru, Wurmspeaker'
	colors.append(constants.GREEN)
	deck_url = 'https://archidekt.com/decks/3255717'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)
	
	colors = []
	#https://archidekt.com/decks/2741782 Minn, Wily Illusionist		Blue
	name = 'Minn, Wily Illusionist'
	colors.append(constants.BLUE)
	deck_url = 'https://archidekt.com/decks/2741782'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)

	colors = []
	#https://archidekt.com/decks/2760019 Mari, the Killing Quill     Black
	name = 'Mari, the Killing Quill'
	colors.append(constants.BLACK)
	deck_url = 'https://archidekt.com/decks/2760019'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)

	colors = []
	#https://archidekt.com/decks/1421091 Thassa, Deep-Dwelling       Blue
	name = 'Thassa, Deep-Dwelling'
	colors.append(constants.BLUE)
	deck_url = 'https://archidekt.com/decks/1421091'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)

	colors = []
	#https://archidekt.com/decks/1506948 Mageta the Lion             White
	name = 'Mageta the Lion'
	colors.append(constants.WHITE)
	deck_url = 'https://archidekt.com/decks/1506948'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)


	colors = []
	#https://archidekt.com/decks/1701465 Meren of Clan Nel Toth      Black, Green
	name = 'Meren of Clan Nel Toth'
	colors.append(constants.BLACK)
	colors.append(constants.GREEN)
	deck_url = 'https://archidekt.com/decks/1701465'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)


	colors = []
	#https://archidekt.com/decks/1432852 Feldon of the Third Path    Red
	name = 'Feldon of the Third Path'
	colors.append(constants.RED)
	deck_url = 'https://archidekt.com/decks/1432852'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)

	colors = []
	#https://archidekt.com/decks/1816083 Aegar, the Freezing Flame   Blue, Red
	name = 'Aegar, the Freezing Flame'
	colors.append(constants.BLUE)
	colors.append(constants.RED)
	deck_url = 'https://archidekt.com/decks/1816083'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)

	colors = []
	#https://archidekt.com/decks/3396654 Imotekh the Stormlord       Black
	name = 'Imotekh the Stormlord'
	colors.append(constants.BLACK)
	deck_url = 'https://archidekt.com/decks/3396654'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)
	
	colors = []
	#https://archidekt.com/decks/3375793 The Swarmlord               Green, Blue, Red
	name = 'The Swarmlord'
	colors.append(constants.GREEN)
	colors.append(constants.BLUE)
	colors.append(constants.RED)
	deck_url = 'https://archidekt.com/decks/3375793'
	commander = Commander(name, colors, deck_url)
	commander_list.append(commander)
	
	return commander_list








