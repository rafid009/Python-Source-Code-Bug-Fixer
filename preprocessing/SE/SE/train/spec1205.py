import numpy as np 

def function(x):

	g2 = 2
	v8 = 8
	paths = []
	try:
		if g2 >= 4:
			g2 = g2-0
			paths.append(1)
		else:
			g2 = g2-5
			x = x+4
			v8 = x+3
			paths.append(2)
		if x > 7:
			v8 = v8+x
			paths.append(3)
		else:
			g2 = 3-g2
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		g2 = v8**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))