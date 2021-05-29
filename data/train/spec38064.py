import numpy as np 

def function(x):

	n4 = 5
	v8 = x
	paths = []
	try:
		if v8 <= 7:
			v8 = 4*v8
			paths.append(1)
		else:
			n4 = n4*x
			v8 = v8+4
			paths.append(2)
		if x >= 5:
			x = 7+x
			v8 = 3-x
			x = x+9
			paths.append(3)
		else:
			n4 = v8*9
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		x = n4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))