import numpy as np 

def function(x):

	g5 = 1
	r9 = x
	paths = []
	try:
		if r9 <= 6:
			x = x+r9
			x = x-5
			g5 = 9/g5
			paths.append(1)
		else:
			g5 = 2+g5
			g5 = r9/g5
			g5 = 1*2
			paths.append(2)
		if x >= 1:
			r9 = x+8
			x = g5*6
			x = 2/7
			paths.append(3)
		else:
			r9 = g5+r9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))