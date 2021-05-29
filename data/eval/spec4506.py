import numpy as np 

def function(x):

	v8 = 9
	g7 = x
	paths = []
	try:
		if x >= 6:
			x = x/7
			g7 = g7+1
			x = x/6
			paths.append(1)
		else:
			v8 = v8+6
			paths.append(2)
		if g7 < 7:
			g7 = 1/g7
			v8 = 6-v8
			x = x/x
			paths.append(3)
		else:
			x = v8-5
			g7 = 1-g7
			v8 = v8-4
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))