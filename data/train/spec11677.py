import numpy as np 

def function(x):

	g7 = x
	r0 = x
	x = 7
	paths = []
	try:
		if g7 <= 9:
			r0 = g7+7
			g7 = 6/g7
			g7 = x+x
			paths.append(1)
		else:
			r0 = r0-5
			paths.append(2)
		if x > 0:
			r0 = r0*3
			paths.append(3)
		else:
			x = x/g7
			g7 = r0-6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))