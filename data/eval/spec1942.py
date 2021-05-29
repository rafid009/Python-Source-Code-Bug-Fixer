import numpy as np 

def function(x):

	v8 = 3
	g9 = x
	paths = []
	try:
		if v8 >= 8:
			x = x*4
			v8 = 2*v8
			v8 = x-v8
			paths.append(1)
		else:
			g9 = 8*g9
			v8 = v8/x
			paths.append(2)
		if v8 < 9:
			x = 2/x
			x = v8+g9
			paths.append(3)
		else:
			v8 = v8+4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))