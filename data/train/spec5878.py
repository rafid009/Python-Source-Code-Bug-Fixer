import numpy as np 

def function(x):

	y6 = x
	j7 = x
	paths = []
	try:
		if y6 <= 1:
			j7 = 7+x
			paths.append(1)
		else:
			x = 6*x
			x = j7/x
			paths.append(2)
		if x <= 5:
			x = 7*x
			x = x-9
			paths.append(3)
		else:
			j7 = j7*j7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		y6 = j7**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))