import numpy as np 

def function(x):

	n4 = x
	j6 = 2
	paths = []
	try:
		if n4 >= 2:
			j6 = 8/n4
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if x <= 9:
			j6 = 2+j6
			paths.append(3)
		else:
			j6 = j6*6
			n4 = 1/n4
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		j6 = n4**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))