import numpy as np 

def function(x):

	f7 = x
	j9 = x
	paths = []
	try:
		if x > 7:
			j9 = 7+j9
			f7 = f7*f7
			f7 = 8*j9
			paths.append(1)
		else:
			x = x+7
			j9 = j9/x
			paths.append(2)
		if j9 >= 4:
			x = x+j9
			x = x/j9
			paths.append(3)
		else:
			x = 9-x
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