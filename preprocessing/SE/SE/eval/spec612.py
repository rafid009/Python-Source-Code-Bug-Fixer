import numpy as np 

def function(x):

	b9 = 0
	v3 = x
	paths = []
	try:
		if x < 6:
			v3 = x+8
			b9 = b9/3
			x = x+5
			paths.append(1)
		else:
			v3 = 9-3
			v3 = 9+9
			paths.append(2)
		if x >= 5:
			x = x*8
			b9 = 7+b9
			v3 = v3/4
			paths.append(3)
		else:
			x = 9*x
			v3 = v3*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v3 = x**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))