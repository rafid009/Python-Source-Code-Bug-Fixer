import numpy as np 

def function(x):

	b9 = x
	v6 = 7
	paths = []
	try:
		if b9 <= 5:
			x = x-v6
			paths.append(1)
		else:
			b9 = 9+b9
			x = b9+3
			v6 = b9/b9
			paths.append(2)
		if b9 <= 1:
			b9 = b9*x
			v6 = 4-5
			x = x/v6
			paths.append(3)
		else:
			b9 = 3+4
			b9 = b9/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))