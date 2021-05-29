import numpy as np 

def function(x):

	j8 = 7
	k2 = 2
	paths = []
	try:
		if j8 > 2:
			k2 = j8-4
			paths.append(1)
		else:
			j8 = j8/x
			paths.append(2)
		if x > 0:
			x = k2/j8
			k2 = 2-k2
			x = x/x
			paths.append(3)
		else:
			k2 = k2-j8
			x = 3-x
			j8 = x-6
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		j8 = j8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))