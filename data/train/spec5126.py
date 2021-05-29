import numpy as np 

def function(x):

	v8 = x
	g4 = x
	paths = []
	try:
		if x < 8:
			v8 = v8/6
			g4 = x-v8
			v8 = v8*9
			paths.append(1)
		else:
			g4 = 4+2
			paths.append(2)
		if x <= 7:
			g4 = 5*5
			paths.append(3)
		else:
			x = v8/x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		g4 = v8**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))