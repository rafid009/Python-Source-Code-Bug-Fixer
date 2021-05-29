import numpy as np 

def function(x):

	v7 = 2
	b9 = x
	paths = []
	try:
		if v7 <= 6:
			v7 = v7+6
			v7 = x-3
			b9 = 6+b9
			paths.append(1)
		else:
			v7 = 9+2
			b9 = b9*7
			v7 = v7-0
			paths.append(2)
		if v7 > 6:
			x = x-v7
			b9 = x/6
			x = v7+x
			paths.append(3)
		else:
			x = x/6
			x = b9*v7
			b9 = 0*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))