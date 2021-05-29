import numpy as np 

def function(x):

	e4 = 8
	j8 = 4
	paths = []
	try:
		if e4 > 6:
			e4 = 2-e4
			paths.append(1)
		else:
			e4 = 5+e4
			x = 9/x
			e4 = e4/j8
			paths.append(2)
		if x <= 3:
			j8 = 1/3
			paths.append(3)
		else:
			x = j8+5
			e4 = 8-9
			e4 = e4-e4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		j8 = e4**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))