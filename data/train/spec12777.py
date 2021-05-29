import numpy as np 

def function(x):

	x3 = x
	v0 = 1
	paths = []
	try:
		if v0 < 9:
			v0 = x3-2
			paths.append(1)
		else:
			x3 = x3*x
			x = 6-x
			paths.append(2)
		if v0 > 9:
			x3 = x3+x
			v0 = x3+v0
			paths.append(3)
		else:
			x = x/x3
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		x3 = v0**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))