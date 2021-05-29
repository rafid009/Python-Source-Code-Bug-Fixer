import numpy as np 

def function(x):

	n7 = 5
	j6 = x
	paths = []
	try:
		if j6 > 3:
			x = 3+6
			paths.append(1)
		else:
			x = 3/j6
			paths.append(2)
		if n7 >= 2:
			j6 = 7/n7
			n7 = n7/1
			j6 = j6+1
			paths.append(3)
		else:
			j6 = 0/j6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))