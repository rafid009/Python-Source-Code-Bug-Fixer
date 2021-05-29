import numpy as np 

def function(x):

	n3 = 7
	j8 = 1
	paths = []
	try:
		if x < 5:
			x = x*4
			n3 = n3/2
			paths.append(1)
		else:
			j8 = j8/3
			n3 = x-j8
			x = 9*x
			paths.append(2)
		if n3 > 6:
			x = 4+x
			paths.append(3)
		else:
			j8 = j8/j8
			n3 = n3-x
			n3 = 4-6
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