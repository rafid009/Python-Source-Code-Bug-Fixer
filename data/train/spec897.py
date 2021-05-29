import numpy as np 

def function(x):

	n9 = 0
	k6 = 0
	paths = []
	try:
		if x < 9:
			n9 = n9+x
			paths.append(1)
		else:
			x = x*3
			n9 = n9-6
			paths.append(2)
		if k6 >= 1:
			k6 = k6-7
			k6 = 1/k6
			paths.append(3)
		else:
			x = x/5
			n9 = n9*n9
			n9 = n9-n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))