from collections import OrderedDict
#有序字典
favorite_languages= OrderedDict()

favorite_languages['jen']='python'
favorite_languages['sarah']='C'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name,language in favorite_languages.items():
	print(name.title()+"'s favorite language is "+
		language.title()+".")
