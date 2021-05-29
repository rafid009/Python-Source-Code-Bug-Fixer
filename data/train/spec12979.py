import numpy as np 

def function(x):

	j8 = 7
	j4 = 3
	paths = []
	try:
		if j8 > 7:
			j8 = j8/j4
			x = 4*x
			paths.append(1)
		else:
			x = x-3
			paths.append(2)
		if j8 <= 9:
			j8 = j8-2
			j8 = x-j8
			j4 = j8/j4
			paths.append(3)
		else:
			j8 = j4+4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j8 = j4**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))