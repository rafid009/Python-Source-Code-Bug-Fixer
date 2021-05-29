import numpy as np 

def function(x):

	x3 = x
	j3 = 5
	paths = []
	try:
		if x3 > 7:
			x3 = 0-6
			j3 = 1*j3
			x = x*x
			paths.append(1)
		else:
			x = 3*x
			j3 = j3*x
			paths.append(2)
		if x3 < 1:
			j3 = j3-0
			x = x3/7
			x3 = j3*7
			paths.append(3)
		else:
			x3 = x3/j3
			x3 = x3/6
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))