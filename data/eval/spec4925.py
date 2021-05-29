import numpy as np 

def function(x):

	n6 = 7
	j8 = 8
	paths = []
	try:
		if x < 4:
			n6 = 6/j8
			paths.append(1)
		else:
			j8 = j8*0
			j8 = x*9
			paths.append(2)
		if x >= 6:
			j8 = j8+n6
			paths.append(3)
		else:
			j8 = j8/8
			j8 = 8*j8
			n6 = n6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))