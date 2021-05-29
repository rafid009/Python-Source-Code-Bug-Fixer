import numpy as np 

def function(x):

	d2 = x
	j8 = 3
	paths = []
	try:
		if x > 7:
			j8 = d2+1
			paths.append(1)
		else:
			x = x/5
			x = 7*3
			x = 6-x
			paths.append(2)
		if d2 >= 8:
			j8 = 3/j8
			paths.append(3)
		else:
			x = x-d2
			j8 = j8-7
			x = x-8
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