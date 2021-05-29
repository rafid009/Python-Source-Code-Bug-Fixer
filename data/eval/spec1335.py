import numpy as np 

def function(x):

	p5 = x
	y0 = x
	paths = []
	try:
		if p5 <= 6:
			y0 = y0-1
			x = x-0
			paths.append(1)
		else:
			y0 = x+3
			paths.append(2)
		if x <= 4:
			y0 = y0+9
			x = 4*0
			paths.append(3)
		else:
			p5 = p5+8
			y0 = y0*0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))