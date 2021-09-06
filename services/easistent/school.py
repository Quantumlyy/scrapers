import re

import lxml.html
import requests

from services.easistent.data import School

BASE_URL = "https://www.easistent.com/urniki/"

class_url_id_regex = re.compile(r"(?:(?:https?:\/\/)?(?:www\.)?easistent\.com\/urniki\/)?(?P<code>[0-9a-f]{40})")
school_id_regex = re.compile(r".+?var id_sola = '(\d+)';")


def get_school_info(school: str) -> School:
	match = re.search(class_url_id_regex, school)

	html = requests.get(BASE_URL + match.group("code")).text
	dom = lxml.html.document_fromstring(html)

	classes = {}
	for el in dom.cssselect("#id_parameter option"):
		classes[el.text] = int(el.attrib["value"])

	school = dom.cssselect("#okvir_prijava h1")[0].text_content()
	scripts = "\n".join([s.text_content() for s in dom.cssselect("script")])

	school_id = int(re.findall(school_id_regex, scripts)[0])

	return School(name=school, classes=classes, id=school_id)
