import numpy as np 

def function(x):

	j8 = x
	n7 = x
	paths = []
	try:
		if n7 > 2:
			j8 = x+j8
			x = 1*x
			paths.append(1)
		else:
			x = x/j8
			paths.append(2)
		if x < 4:
			j8 = 0+j8
			j8 = 6*7
			paths.append(3)
		else:
			n7 = n7/2
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		j8 = n7**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))