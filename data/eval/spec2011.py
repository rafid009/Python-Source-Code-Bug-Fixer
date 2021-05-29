import numpy as np 

def function(x):

	p5 = 6
	g5 = 8
	x = x
	paths = []
	try:
		if x < 1:
			g5 = g5-x
			paths.append(1)
		else:
			x = x+x
			x = 8+x
			g5 = 8+2
			paths.append(2)
		if p5 <= 4:
			g5 = g5+x
			x = x+6
			paths.append(3)
		else:
			x = x-7
			p5 = x-6
			g5 = x+9
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))