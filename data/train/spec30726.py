import numpy as np 

def function(x):

	n8 = x
	j8 = 2
	paths = []
	try:
		if n8 > 9:
			x = x*n8
			j8 = 3/j8
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if x > 1:
			x = x+7
			j8 = j8*4
			j8 = j8/j8
			paths.append(3)
		else:
			j8 = n8/j8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		j8 = n8**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))