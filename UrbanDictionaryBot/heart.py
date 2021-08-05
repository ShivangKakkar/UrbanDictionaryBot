import random
import re
from udpy import AsyncUrbanClient

ud = AsyncUrbanClient()


async def newify(text: str):
	pattern = r"[\[\]]"
	string = re.sub(pattern, "", text)
	mod_string = ". ".join(i.capitalize() for i in string.split(". "))
	mod2_string = "\n\n".join(i.capitalize() for i in mod_string.split("\n\n"))
	new_string = ":".join(i.capitalize() for i in mod2_string.split(":"))
	return new_string


async def ud_search(text: str):
	defs = await ud.get_definition(text)
	try:
		info = random.choice(defs)
		word = info.word.capitalize()
		definition = await newify(info.definition)
		example = await newify(info.example)
		rep = f"**Word** `{word}` \n\n**Definition** \n{definition} \n\n**Example** \n{example}"
	except IndexError:
		if len(text) >= 100:
			rep = "Don't try to search paragraphs"
			word = "Query Not Found"
		else:
			rep = "Query Not Found: Doesn't exist in Urban Dictionary"
			word = "Query Not Found"
	return word, rep;


async def rand():
	rand_def = await ud.get_random_definition()
	info = random.choice(rand_def)
	word = info.word.capitalize()
	definition = await newify(info.definition)
	example = await newify(info.example)
	rand_str = f"**Random Word** `{word}` \n\n**Definition** \n{definition} \n\n**Example** \n{example}"
	return word, rand_str;