import numpy as np 

def function(x):

	h3 = x
	j8 = 2
	paths = []
	try:
		if h3 >= 0:
			x = j8*x
			paths.append(1)
		else:
			h3 = 2-6
			j8 = x+1
			j8 = 2+j8
			paths.append(2)
		if x >= 9:
			h3 = 0/h3
			h3 = 4*6
			paths.append(3)
		else:
			h3 = 4+5
			x = x/6
			h3 = h3*7
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