import numpy as np 

def function(x):

	a3 = 5
	j8 = x
	paths = []
	try:
		if a3 < 2:
			j8 = 0*4
			j8 = j8*3
			j8 = j8*j8
			paths.append(1)
		else:
			j8 = j8*4
			paths.append(2)
		if a3 >= 4:
			j8 = j8+3
			paths.append(3)
		else:
			x = 8*9
			a3 = a3/j8
			x = x*x
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))