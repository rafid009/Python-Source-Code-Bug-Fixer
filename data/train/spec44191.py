import numpy as np 

def function(x):

	j7 = x
	n6 = x
	paths = []
	try:
		if j7 < 5:
			j7 = x+j7
			n6 = j7*x
			paths.append(1)
		else:
			x = 3/2
			x = 6/x
			paths.append(2)
		if j7 <= 7:
			n6 = n6-4
			x = 1*n6
			n6 = 4-n6
			paths.append(3)
		else:
			j7 = j7/7
			n6 = n6*n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))