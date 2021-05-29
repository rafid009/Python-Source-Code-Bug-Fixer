import numpy as np 

def function(x):

	j7 = 5
	n9 = 9
	paths = []
	try:
		if j7 <= 3:
			x = x-x
			paths.append(1)
		else:
			n9 = n9/2
			j7 = 0+j7
			paths.append(2)
		if j7 < 2:
			j7 = x/8
			paths.append(3)
		else:
			n9 = j7*n9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))