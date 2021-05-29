import numpy as np 

def function(x):

	r9 = x
	j8 = 9
	paths = []
	try:
		if j8 < 0:
			r9 = r9*r9
			r9 = 2+x
			paths.append(1)
		else:
			j8 = j8+1
			j8 = 7+5
			paths.append(2)
		if j8 > 7:
			r9 = 1-r9
			paths.append(3)
		else:
			x = 5-6
			r9 = r9-3
			j8 = r9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r9 = x**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))