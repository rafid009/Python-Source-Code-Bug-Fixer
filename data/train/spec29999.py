import numpy as np 

def function(x):

	j8 = 0
	paths = []
	try:
		if x <= 4:
			x = x+5
			j8 = j8/7
			j8 = j8/5
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if j8 <= 8:
			j8 = j8/2
			paths.append(3)
		else:
			x = x-x
			x = 6-0
			x = 5*j8
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