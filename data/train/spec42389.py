import numpy as np 

def function(x):

	u2 = x
	j3 = x
	x = x
	paths = []
	try:
		if j3 >= 4:
			x = x/u2
			x = x+u2
			x = u2-3
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if j3 < 2:
			x = u2/8
			u2 = 8/u2
			u2 = 5/1
			paths.append(3)
		else:
			u2 = 3-u2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))