# TrevorBot
An IRC bot to help people never forget Trevor #TrevorForget. tl;dr. This project is mostly a joke.
The code found here is a irc bot that by default goes by the name of TrevorBot.

Default config:
Server: chat.freenode.net
Bot Nick: TrevorBot
Admin Nick: None
Channel: #Freenode
port: 6667


All feedback is welcome!

Usage:

	python bot.py

Optional:

	python bot.py <Admin Nick> <channels to connect to> <Bot Nick> <Server> <Port>

Common commands:
	.stop : Makes the bot quit if issued by bot administrator

Keywords:

	hello : responds with 'Hi (name)!'
	roach, cockroach : Responds with '#TrevorForget! https://www.csoonline.com/article/3227910/security/hackers-create-memorial-for-a-cockroach-named-trevor.html'
	trevor : Responds with '@(name) I'm sad too, but Trevor will always live on in our hearts. #TrevorForget'

Actions:

	On user join : Responds with 'Welcome (name) #TrevorForget'

To come in future updates:

	More commands
	Keep track of the amount of time's trevor is mentioned
	Create a leaderboard for how many times someone has said the word trevor.

ChangeLog:

	Added ChangeLog
	Created Branch 1.1 : Branch will be build of bot that reads from config.txt and uses options for bot.py, will also support arguments provided from cli.