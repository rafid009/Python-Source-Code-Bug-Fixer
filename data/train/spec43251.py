import numpy as np 

def function(x):

	v0 = x
	j8 = 1
	paths = []
	try:
		if v0 > 9:
			v0 = 9*6
			paths.append(1)
		else:
			v0 = v0*4
			j8 = j8/8
			paths.append(2)
		if v0 <= 1:
			v0 = v0+1
			paths.append(3)
		else:
			j8 = 2/8
			j8 = j8-9
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