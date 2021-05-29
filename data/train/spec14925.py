import numpy as np 

def function(x):

	n5 = 3
	e9 = x
	paths = []
	try:
		if n5 <= 8:
			x = x/8
			paths.append(1)
		else:
			n5 = x/n5
			paths.append(2)
		if e9 <= 2:
			e9 = x-5
			paths.append(3)
		else:
			n5 = n5+8
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))