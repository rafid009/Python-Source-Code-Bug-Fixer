import numpy as np 

def function(x):

	j8 = x
	j5 = 3
	paths = []
	try:
		if j8 <= 7:
			x = j8-3
			paths.append(1)
		else:
			j8 = x+j8
			x = 2-x
			j5 = 8+j5
			paths.append(2)
		if j8 < 3:
			j8 = x/j8
			paths.append(3)
		else:
			j8 = j8/3
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