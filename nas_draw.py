import turtle
import PIL
from PIL import Image
import time

images = [['nas.gif'], ['ericb_rakim.gif', 'fugees.gif', 'gza.gif', 'raekwon.gif', 'wutang.gif', 'jayz.gif', 'blackstar.gif', 'tribe_theory.gif'], ['aaliyah.gif', 'thought.gif', 'badu.gif', 'baker.gif', 'bdp.gif', 'beatles.gif', 'biggie.gif', 'bigl.gif', 'biz.gif', 'atliens.gif', 'bob.gif', 'bobby_digital.gif', 'bunb.gif', 'burrel.gif', 'canibus.gif', 'capitalpun.gif', 'chance.gif', 'childish_gambino.gif', 'cube.gif', 'curtis.gif', 'delasoul.gif', 'diddy.gif', 'donuts.gif', 'doom.gif', 'dre.gif', 'electronica.gif', 'em.gif', 'wayne.gif', 'finesse.gif', 'quas.gif', 'ghostface.gif', 'gkmc.gif', 'pharcyde.gif', 'jamesbrown.gif', 'thecool.gif', 'jcole.gif', 'jermaine_jackson.gif', 'jorge_1976_africa.gif', 'laurynhill.gif', 'lecrae.gif', 'lonnie.gif', 'lonnie2.gif', 'lupefiasco.gif', 'madvillian.gif', 'main_source.gif', 'marciano.gif', 'mgaye.gif', 'mobb_deep.gif', 'mos_def.gif', 'new_danger.gif', 'nwa.gif', 'oxymoron.gif', 'pe.gif', 'pete_rock.gif', 'ross.gif', 'rundmc.gif', 'shining.gif', 'slumvillage.gif', 'stevie.gif', 'streetsiswatching.gif', 'tarika_blue.gif', 'temptations.gif', 'willie.gif', 'tmonk.gif'], ['rbgflag.gif'], ['pick.gif']]

def resize_img(filename, basewidth):
	img = Image.open(filename)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	resized_img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
	words = filename.split('.')
	words[0] += '-resized'
	resized_img.save('.'.join(words))
	return '.'.join(words)

def collage(width, curr_depth, index, points, max_depth):
	global images
	if curr_depth < max_depth:
		myPen = turtle.Turtle()
		myPen.speed(0)
		myPen.penup()
		myPen.goto(points[0], points[1])
		myPen.pendown()

		if curr_depth > 2:
			filename = images[curr_depth][0]
		else:
			filename = images[curr_depth][index]

		img_resized = resize_img(filename, width)

		# add the shape first then set the turtle shape
		if img_resized not in screen.getshapes():
			screen.addshape(img_resized)
		myPen.shape(img_resized)

		nwidth = width / 3
		radius = width / 2
		nradius = nwidth / 2

		collage(nwidth, curr_depth + 1, index * 8 + 0, (points[0], points[1] + radius + nwidth + nradius), max_depth)
		collage(nwidth, curr_depth + 1, index * 8 + 1, (points[0] + radius + nwidth + nradius, points[1]), max_depth)
		collage(nwidth, curr_depth + 1, index * 8 + 2, (points[0], points[1] - (radius + nwidth + nradius)), max_depth)
		collage(nwidth, curr_depth + 1, index * 8 + 3, (points[0] - (radius + nwidth + nradius), points[1]), max_depth)
		collage(nwidth, curr_depth + 1, index * 8 + 4, (points[0] + radius + nwidth + nradius, points[1] + radius + nwidth + nradius), max_depth)
		collage(nwidth, curr_depth + 1, index * 8 + 5, (points[0] - (radius + nwidth + nradius), points[1] - (radius + nwidth + nradius)), max_depth)
		collage(nwidth, curr_depth + 1, index * 8 + 6, ((points[0] + radius + nwidth + nradius), points[1] - (radius + nwidth + nradius)), max_depth)
		collage(nwidth, curr_depth + 1, index * 8 + 7, (points[0] - (radius + nwidth + nradius), points[1] + radius + nwidth + nradius), max_depth)

def collage_helper(width, max_depth):
	collage(width, 0, 0, (0,0), max_depth)

if __name__ == "__main__":
	while True:
		screen = turtle.Screen()
		screen.setup(width=0.95, height=0.95)
		collage_helper(300, 5)
		screen.bgcolor("lightblue")
	
		time.sleep(30)
		screen.clearscreen()
