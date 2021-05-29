import numpy as np 

def function(x):

	x5 = 8
	j9 = x
	paths = []
	try:
		if j9 > 0:
			x5 = x5*7
			paths.append(1)
		else:
			x5 = x5+2
			paths.append(2)
		if x < 2:
			x5 = x5+j9
			j9 = 6-x
			j9 = 6-0
			paths.append(3)
		else:
			j9 = 2+j9
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		j9 = x5**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))