import numpy as np 

def function(x):

	j3 = x
	z9 = 7
	paths = []
	try:
		if x > 4:
			x = x/4
			j3 = j3/j3
			paths.append(1)
		else:
			x = z9/9
			paths.append(2)
		if z9 >= 4:
			x = x+j3
			paths.append(3)
		else:
			x = 1*x
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