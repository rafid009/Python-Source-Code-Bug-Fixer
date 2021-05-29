import numpy as np 

def function(x):

	j9 = 1
	n3 = 5
	paths = []
	try:
		if n3 < 0:
			j9 = 8/j9
			paths.append(1)
		else:
			n3 = j9+x
			paths.append(2)
		if x > 4:
			x = x/j9
			n3 = n3*1
			x = 3/4
			paths.append(3)
		else:
			j9 = j9*5
			x = x-j9
			j9 = 6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))