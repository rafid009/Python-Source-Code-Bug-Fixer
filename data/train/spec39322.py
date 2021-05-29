import numpy as np 

def function(x):

	v8 = x
	j9 = x
	paths = []
	try:
		if x <= 5:
			j9 = 0/1
			paths.append(1)
		else:
			x = 1-7
			j9 = j9-8
			j9 = j9+2
			paths.append(2)
		if x > 3:
			x = x/6
			x = 1*x
			v8 = v8*j9
			paths.append(3)
		else:
			v8 = 4-x
			j9 = j9*5
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