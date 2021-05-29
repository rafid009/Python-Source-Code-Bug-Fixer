import numpy as np 

def function(x):

	j8 = 6
	d8 = 8
	paths = []
	try:
		if j8 > 8:
			x = d8+d8
			paths.append(1)
		else:
			j8 = d8/j8
			paths.append(2)
		if x <= 9:
			j8 = 8+d8
			x = 4-x
			paths.append(3)
		else:
			j8 = j8-2
			x = x*5
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		d8 = j8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))