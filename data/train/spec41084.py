import numpy as np 

def function(x):

	p5 = x
	y2 = 9
	paths = []
	try:
		if p5 < 4:
			y2 = x+p5
			x = x/9
			y2 = p5/x
			paths.append(1)
		else:
			y2 = 7/p5
			y2 = x/6
			paths.append(2)
		if p5 >= 8:
			x = x/x
			paths.append(3)
		else:
			x = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p5 = x**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))