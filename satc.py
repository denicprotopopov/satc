import requests, bs4, webbrowser, sys, time, random, os

def main():
	seasons = random.randrange(1, 7)
	if seasons == 1:
		episodes = random.randrange(1, 13)
	elif seasons == 5:
		episodes = random.randrange(1, 9)
	elif seasons == 6:
		episodes = random.randrange(1, 21)
	else:
		episodes = random.randrange(1, 19)
	get_movie(seasons, episodes)
	im_feeling_lucky(seasons, episodes)

def get_movie(seasons, episodes):
	season = seasons
	episode = episodes
	os.system("say 'oh my god looks like we are going to watch season'" + str(season) + "episode" + str(episode) + "of sex and the city. again")
	return season, episode

def im_feeling_lucky(season, episode):
	if episode < 9:
		webbrowser.open('https://fenglish.ru/movie/sex_and_the_city-s0' + str(season) + 'e0' + str(episode))
	else:
		webbrowser.open('https://fenglish.ru/movie/sex_and_the_city-s0' + str(season) + 'e' + str(episode))

	time.sleep(0.5)
main()
