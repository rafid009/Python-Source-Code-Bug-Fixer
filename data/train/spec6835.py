import numpy as np 

def function(x):

	g4 = x
	p5 = x
	paths = []
	try:
		if x < 2:
			g4 = p5+4
			x = 8-5
			p5 = p5-x
			paths.append(1)
		else:
			x = x-x
			p5 = x-2
			paths.append(2)
		if p5 >= 7:
			x = g4*0
			p5 = p5/p5
			g4 = 5+p5
			paths.append(3)
		else:
			g4 = g4/p5
			p5 = p5+6
			x = 0*p5
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		p5 = g4**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))