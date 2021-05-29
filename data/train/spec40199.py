import numpy as np 

def function(x):

	r3 = 9
	v9 = 7
	paths = []
	try:
		if x <= 3:
			r3 = 3+x
			r3 = r3-1
			paths.append(1)
		else:
			r3 = 9*r3
			x = 3+r3
			paths.append(2)
		if x <= 4:
			r3 = r3+7
			r3 = v9*r3
			x = x+7
			paths.append(3)
		else:
			r3 = r3-9
			x = r3+x
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