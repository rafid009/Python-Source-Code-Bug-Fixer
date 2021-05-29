import numpy as np 

def function(x):

	v9 = 7
	i7 = 3
	paths = []
	try:
		if v9 <= 8:
			v9 = i7+3
			paths.append(1)
		else:
			i7 = 8*0
			x = x/x
			paths.append(2)
		if v9 > 2:
			i7 = i7-6
			v9 = v9-x
			paths.append(3)
		else:
			v9 = x+3
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