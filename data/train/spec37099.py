import numpy as np 

def function(x):

	k1 = 9
	n9 = 0
	paths = []
	try:
		if k1 >= 4:
			n9 = n9-9
			n9 = x/5
			k1 = k1/4
			paths.append(1)
		else:
			k1 = 4/k1
			x = 8+2
			n9 = 6-5
			paths.append(2)
		if k1 >= 4:
			n9 = n9-7
			paths.append(3)
		else:
			x = 2-x
			k1 = k1/3
			k1 = k1*6
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