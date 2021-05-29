import numpy as np 

def function(x):

	x3 = x
	j2 = x
	paths = []
	try:
		if x > 3:
			j2 = j2+2
			paths.append(1)
		else:
			x3 = 6+x3
			x = 4*x
			paths.append(2)
		if j2 >= 0:
			x = 9+j2
			paths.append(3)
		else:
			x = 6*x3
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