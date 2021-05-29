import numpy as np 

def function(x):

	f7 = 3
	j8 = x
	paths = []
	try:
		if j8 < 4:
			j8 = 7/5
			x = x*x
			paths.append(1)
		else:
			j8 = f7-x
			x = x-x
			x = 4*x
			paths.append(2)
		if x <= 9:
			x = f7+x
			j8 = 1+j8
			paths.append(3)
		else:
			f7 = f7*f7
			x = 4-x
			j8 = x*4
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