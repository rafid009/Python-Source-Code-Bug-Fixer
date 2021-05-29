import numpy as np 

def function(x):

	j9 = 7
	e3 = 1
	x = 8
	paths = []
	try:
		if x >= 3:
			x = x*j9
			j9 = x/j9
			e3 = e3/7
			paths.append(1)
		else:
			j9 = 5-3
			j9 = 5/e3
			paths.append(2)
		if j9 < 0:
			j9 = 7+e3
			paths.append(3)
		else:
			j9 = 0*x
			e3 = e3-7
			j9 = x+1
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))