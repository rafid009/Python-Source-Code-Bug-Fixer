import numpy as np 

def function(x):

	y3 = x
	g3 = 5
	paths = []
	try:
		if y3 > 5:
			y3 = 4+8
			g3 = g3-y3
			paths.append(1)
		else:
			x = x+y3
			paths.append(2)
		if y3 <= 8:
			g3 = g3+6
			y3 = y3+0
			x = x/1
			paths.append(3)
		else:
			y3 = x/5
			y3 = x*8
			g3 = g3-8
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))