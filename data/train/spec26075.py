import numpy as np 

def function(x):

	g4 = 8
	p8 = x
	paths = []
	try:
		if x <= 2:
			x = x+p8
			p8 = 3/9
			p8 = p8+9
			paths.append(1)
		else:
			g4 = 5-x
			g4 = 7+g4
			x = 1*x
			paths.append(2)
		if x <= 1:
			g4 = g4*8
			paths.append(3)
		else:
			p8 = 0-4
			x = x-x
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		p8 = p8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))