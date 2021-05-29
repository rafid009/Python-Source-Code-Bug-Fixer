import numpy as np 

def function(x):

	i7 = 8
	j8 = 7
	paths = []
	try:
		if x < 8:
			i7 = 0*3
			paths.append(1)
		else:
			i7 = i7+i7
			i7 = i7/x
			paths.append(2)
		if j8 < 2:
			i7 = 1-i7
			paths.append(3)
		else:
			i7 = i7+8
			i7 = i7/7
			j8 = 5-j8
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