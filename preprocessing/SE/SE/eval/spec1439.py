import numpy as np 

def function(x):

	v9 = 4
	b1 = 2
	x = x
	paths = []
	try:
		if v9 < 7:
			v9 = v9-v9
			paths.append(1)
		else:
			b1 = v9-b1
			v9 = v9+x
			v9 = v9-v9
			paths.append(2)
		if v9 > 6:
			b1 = b1*6
			x = x-9
			paths.append(3)
		else:
			v9 = v9*8
			v9 = v9-v9
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))