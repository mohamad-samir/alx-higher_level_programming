all: exec semi_check

exec:
	chmod +x *.js

semi_check_all:
	semistandard --verbose | snazzy

semi_check:
	semistandard $$(ls | grep .js | grep -v main.js) --verbose | snazzy

fix_semi:
	semistandard $$(ls | grep .js | grep -v main.js) --fix
