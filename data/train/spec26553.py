import numpy as np 

def function(x):

	e0 = 3
	j9 = x
	paths = []
	try:
		if x < 9:
			j9 = j9*3
			x = 8+x
			e0 = e0+8
			paths.append(1)
		else:
			e0 = e0-5
			paths.append(2)
		if x >= 4:
			e0 = 2/e0
			j9 = 6+j9
			e0 = 6/e0
			paths.append(3)
		else:
			e0 = x/5
			e0 = e0*2
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