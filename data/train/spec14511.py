import numpy as np 

def function(x):

	x8 = x
	v5 = 2
	paths = []
	try:
		if v5 > 2:
			v5 = v5+3
			x8 = x8+0
			paths.append(1)
		else:
			x = 9+0
			paths.append(2)
		if v5 > 2:
			x = 5*x
			x = x/v5
			v5 = 4-v5
			paths.append(3)
		else:
			x = x+x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		v5 = x8**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))