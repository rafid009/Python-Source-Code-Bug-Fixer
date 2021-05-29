import numpy as np 

def function(x):

	g6 = x
	v8 = x
	paths = []
	try:
		if g6 <= 1:
			g6 = g6+x
			x = 9/8
			v8 = v8-x
			paths.append(1)
		else:
			g6 = 8*x
			x = 5*v8
			x = x-1
			paths.append(2)
		if x >= 4:
			g6 = 8/v8
			x = x+x
			paths.append(3)
		else:
			g6 = g6*v8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))