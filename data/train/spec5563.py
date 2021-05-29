import numpy as np 

def function(x):

	y3 = 5
	j8 = x
	paths = []
	try:
		if j8 < 6:
			j8 = j8-4
			x = x*8
			paths.append(1)
		else:
			y3 = 2*7
			x = x/6
			y3 = y3+1
			paths.append(2)
		if j8 > 3:
			y3 = j8/y3
			paths.append(3)
		else:
			y3 = x*j8
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