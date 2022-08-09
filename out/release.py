# this python script generates patch folders that can be read by Tango, using a minimal amount of manually supplied info.
# to get the python runtime, search "python" in the Microsoft Store:tm: and blindly install the first result.

# edit the folder with the '_base.toml' suffix to include the proper patch info such as title, author, source.
# do not include any version info or manually change the '_versions.toml' file. This will all be managed procedurally.
# (unless you need to delete some accidental stuff from the _versions.toml file)

# edit the variables at the top of this file to use the details for your patch

# call this script by opening a cmd window in the same directory as it and running 'python release.py' (without the quotes)
# then when prompted, enter the version number for this release. Example: 1.0.0


games = ["bn4",]	# must be manually defined, values are comma separated
patchname = "sus"		# must be manually defined, game name is prepended to it
AlwaysPromptForCompatibilityString = True	# set to false if patch updates don't break compatibility
netplay_compatibility = "" # game name is prepended to it, this will be overwritten at runtime if the above boolean is True
patchnames = {
	"bn4": ["MEGAMANBN4BMB4BE_00.bps",], # must be manually defined
}


import os
import sys
import re
import shutil

# this var should only enabled if a '_saveedit.txt' file is also included,
# which tango uses to override default text characters when deciding 
# how to display chip names, etc in the save viewer.
HasCharacterOverrides = False

txt = ""		# this page left intentionally blank
base = ""		# this page left intentionally blank
latest = ""		# this page left intentionally blank
overrides = ""	# this page left intentionally blank

for game in games:
	try:
		# load _versions file into memory and fetch the latest version number to print out
		with open("tango_patches/{}_versions.toml".format(game), 'r', encoding = 'utf-8') as file:
			txt = file.read()
			latest = re.findall("(?<=')\d\.\d\.\d(?='\])",txt)
			if len(latest) > 0:
				latest = latest[len(latest)-1]
			else:
				latest = "none"

		# get input from user in format X.Y.Z
		sys.stdout.write("New {} version? Latest Ver = {} \nFormat = X.Y.Z \n".format(game,latest))
		version = input()


		# manage netplay compatibility string
		if AlwaysPromptForCompatibilityString == True:
			sys.stdout.write("netplay_compatibility string: \n".format(game,latest))
			netplay_compatibility = input()
		else:
			if len(netplay_compatibility) > 0:
				sys.stdout.write("netplay version: \"{}\" (you can update it by editing this file) \n".format(netplay_compatibility))
			else:
				sys.stdout.write("netplay_compatibility string is not defined. This better be on purpose.\n".format(netplay_compatibility))

	except IOError:
		print("_versions: Could not open file.")
		continue

	if HasCharacterOverrides == True:
		try:
			with open("tango_patches/{}_saveedit.txt".format(game), 'r', encoding = 'utf-8') as file:
				overrides = file.read()
		except IOError:
			print("_saveedit: Could not open file.")
			continue

	try:
		with open("tango_patches/{}_versions.toml".format(game), 'a', encoding = 'utf-8') as file:

			# skip if user input is obviously invalid
			if version == "" or len(version) < 5:
				continue
			append = "[versions.'{}']\n".format(version)
			if HasCharacterOverrides == True:
				append += "saveedit_overrides = {{ charset = [{}] }}\n".format(overrides)
			append += "netplay_compatibility = \"{}{}\"\n".format(game,netplay_compatibility)
			txt += append
			file.write(append)
	except IOError:
		print("_versions: Could not open file.")
		continue

	# load the base of the info.toml file
	try:
		with open("tango_patches/{}_base.toml".format(game), 'r') as file:
			base = file.read()

	except IOError:
		print("_base: Could not open file.")
		continue

	txt = base + txt
	path = "tango_patches/{}{}".format(game,patchname)

	if not os.path.exists(path):
		os.mkdir(path,0o666)
	folderpath = "{}/v{}".format(path,version)
	if not os.path.exists(folderpath):
		os.mkdir(folderpath,0o666)

	newfile = open("{}/info.toml".format(path), 'w', encoding = 'utf-8')
	bb = newfile.write(txt)
	newfile.close()

	for name in patchnames[game]:
		shutil.copy(name,"{}/{}".format(folderpath,name))

	sys.stdout.write("\nSUCCESS: {}{} v{} created in path \"{}/\"\n\n".format(game,patchname,version,folderpath))