import numpy as np 

def function(x):

	i5 = x
	x9 = x
	paths = []
	try:
		if i5 <= 5:
			i5 = x9-4
			paths.append(1)
		else:
			x = i5*x9
			i5 = x9/9
			paths.append(2)
		if x9 <= 9:
			x9 = x9+x9
			x = x+4
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x = x9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))