import numpy as np 

def function(x):

	v7 = x
	b3 = 6
	paths = []
	try:
		if b3 <= 5:
			v7 = v7+6
			paths.append(1)
		else:
			v7 = x+b3
			v7 = v7-7
			paths.append(2)
		if b3 > 3:
			v7 = 9/v7
			v7 = 9/5
			paths.append(3)
		else:
			v7 = v7/2
			v7 = v7/3
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