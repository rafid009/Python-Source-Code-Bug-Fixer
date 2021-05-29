import numpy as np 

def function(x):

	j9 = x
	r9 = x
	paths = []
	try:
		if j9 < 4:
			x = j9+r9
			r9 = x/8
			paths.append(1)
		else:
			j9 = 4*7
			x = 6*x
			j9 = j9*r9
			paths.append(2)
		if x <= 0:
			j9 = 7-j9
			x = 7+x
			r9 = x-r9
			paths.append(3)
		else:
			j9 = 6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))