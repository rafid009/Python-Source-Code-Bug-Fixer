import numpy as np 

def function(x):

	i6 = 4
	e9 = x
	paths = []
	try:
		if e9 > 1:
			x = 3+9
			e9 = e9-8
			e9 = i6+3
			paths.append(1)
		else:
			x = 4-8
			paths.append(2)
		if e9 >= 4:
			e9 = e9+2
			paths.append(3)
		else:
			i6 = 5-i6
			x = x*6
			i6 = i6+i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))