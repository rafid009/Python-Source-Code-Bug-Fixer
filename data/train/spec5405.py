import numpy as np 

def function(x):

	g0 = x
	b9 = x
	paths = []
	try:
		if x < 9:
			x = x+x
			b9 = 1/b9
			x = x/6
			paths.append(1)
		else:
			g0 = g0*5
			g0 = g0+6
			x = x-9
			paths.append(2)
		if g0 <= 7:
			x = b9-5
			x = 1+8
			paths.append(3)
		else:
			x = g0*4
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))