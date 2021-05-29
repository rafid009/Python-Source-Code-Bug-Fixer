import numpy as np 

def function(x):

	j8 = 6
	j4 = 7
	paths = []
	try:
		if x >= 7:
			j4 = 9/j4
			j4 = j4+7
			x = 9+x
			paths.append(1)
		else:
			x = x/9
			x = 8-4
			j8 = j8-j4
			paths.append(2)
		if j8 >= 5:
			x = x*j8
			x = 9-j8
			paths.append(3)
		else:
			j8 = j8/x
			x = 9-8
			j4 = j4-x
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