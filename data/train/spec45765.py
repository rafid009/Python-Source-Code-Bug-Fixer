import numpy as np 

def function(x):

	r8 = x
	v2 = 8
	paths = []
	try:
		if r8 <= 0:
			x = 4/x
			x = 0+4
			r8 = r8+v2
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if x < 7:
			x = 1*x
			x = v2/x
			r8 = r8+v2
			paths.append(3)
		else:
			r8 = r8-r8
			x = 4+9
			r8 = 8+v2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))