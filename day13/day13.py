from typing import Dict, List, Tuple
import base64


cp = {
	'.': '  ',
	'#': '██'
}

def pg(cd, ymx, xmx) -> List[str]:
	lines = []
	for j in range(ymx):
		line = ''
		for i in range(xmx):
			line += cp[cd[(j,i)]]
		lines.append(line)
	print('\n'.join(lines))
	return lines

def dc(cd, ymx, xmx) -> int:
	dc = 0
	for j in range(ymx):
		for i in range(xmx):
			if cd[(j,i)] == '#':
				dc += 1
	return dc


def fold_y(amt: int,x_max: int ,y_max: int, cd: Dict[Tuple[int, int], str]) -> Tuple[int, Dict[Tuple[int, int], str]]:
	real_fold = amt - 1
	new_cd = {}
	yb2 = y_max // 2
	if yb2 <= amt <= yb2 + 1:
		for j in range(y_max):
			for i in range(x_max):
				if j > real_fold:
					v = cd[(j,i)]
					if v == '#':
						new_cd[(abs(j - (2 * amt)), i)] = '#' 
				else:
					new_cd[(j,i)] = cd[(j,i)]
		nymax = amt
		return nymax, new_cd
	else:
		raise Exception('NOOOO')

def fold_x(amt: int,x_max: int ,y_max: int, cd: Dict[Tuple[int, int], str]) -> Tuple[int, Dict[Tuple[int, int], str]]:
	real_fold = amt - 1
	new_cd = {}
	xb2 = x_max // 2
	if xb2 <= amt <= xb2 + 1:
		for j in range(y_max):
			for i in range(x_max):
				if i > real_fold:
					v = cd[(j,i)]
					if v == '#':
						new_cd[(j, abs(i - (2 * amt)))] = '#' 
				else:
					new_cd[(j,i)] = cd[(j,i)]
		nxmax = amt
		return nxmax, new_cd
	else:
		raise Exception('NOOOO')


def parser(file) -> Tuple[List[Tuple[int, int]], List[Tuple[str, str]]]:
	cord_list = []
	fold_list = []

	found_break = False
	for line in open(file).readlines():
		if line.strip() == "":
			found_break = True
		else:
			if found_break:
				fold_list.append(line.strip())
			else:
				cord_list.append(line.strip())
	cord_list = [tuple([int(v) for v in cord.split(',')])[::-1] for cord in cord_list]
	fold_list = [tuple(v.split(' ')[-1].split('=')) for v in fold_list]
	return cord_list, fold_list

def make_cd(x_max, y_max) -> Dict[Tuple[int,int], str]:
	cd = {}
	for j in range(y_max):
		for i in range(x_max):
			cd[(j,i)] = '.'
	for v in cord_list:
		cd[v] = '#'
	return cd

def perform_folds(cd, x_max, y_max, fold_list):
	fc = 0
	for fold in fold_list:
		fc += 1
		if fold[0] == 'x':
			x_max, cd = fold_x(int(fold[1]), x_max, y_max, cd)
		elif fold[0] == 'y':
			y_max, cd = fold_y(int(fold[1]), x_max, y_max, cd)
	return cd, x_max, y_max

def PIL_visualize(lines: List[str]) -> Tuple[bool, str]:
	try:
		from PIL import Image, ImageDraw, ImageFont
		from io import BytesIO
	except ImportError:
		print("Need Pillow for Creating Image")
		return False, ""
	else:
		max_w = 3000
		im = Image.new('L',(max_w,max_w),255)
		d = ImageDraw.ImageDraw(im)
		f = ImageFont.truetype('./Inconslata.ttf',size=40)
		w,h = f.getsize(cp["#"])
		ihi = 100
		for line in lines:
			line = line.replace('██','███').replace('  ','   ')
			d.text((100,ihi), line, 0, font=f)
			ihi += h
		newim = im.crop((0,0,max_w,ihi + 100)).convert('RGB')
		bio = BytesIO()
		newim.save(bio, format='PNG')
		newim.save('text_image.png')
		bio.seek(0)
		# "data:image/png;base64," + 
		istr =  base64.b64encode(bio.getvalue()).decode()
		print("=" * 10)
		try:
			import pytesseract
			print(f"OCR: {pytesseract.image_to_string('text_image.png')}")
		except ImportError:
			print("No pytesseract OCR present")
		print("=" * 10)
		return True,istr

def google_ocr(GOOGLE_API_OCR ,istr):
	try:
		import httpx
	except ImportError:
		print("No httpx found. Aborting...")
		return
	else:
		payload = {
			"requests": [
				{
					"image": {
						"content": istr
					},
					"features": [{
						"type": "TEXT_DETECTION"
					}]
				}
			]
		}
		headers = {
            "content-type": "application/json",
            "Accept-Charset": "UTF-8"
        }
		out = httpx.post(f'https://eu-vision.googleapis.com/v1/images:annotate?key={GOOGLE_API_OCR}', json=payload, headers=headers)
		js = out.json()
		print("=" * 10)
		try:
			print(f'Accurate Google OCR: {js["responses"][0]["textAnnotations"][0]["description"].strip()}')
		except KeyError or IndexError:
			print("Failed to get OCR from google")
		print("=" * 10)



if __name__ == '__main__':

	# Get an API key for google Cloud vision. Use here uwu
	GOOGLE_API_OCR = None
	cord_list, fold_list = parser("data.txt")
	x_max = max([cord[1] for cord in cord_list]) + 1
	y_max = max([cord[0] for cord in cord_list]) + 1
	cd = make_cd(x_max, y_max)
	cd, x_max, y_max = perform_folds(cd, x_max, y_max, fold_list)
	lines = pg(cd, y_max, x_max)
	out,istr = PIL_visualize(lines)
	if out and GOOGLE_API_OCR:
		google_ocr(GOOGLE_API_OCR, istr)
	

