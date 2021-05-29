import numpy as np 

def function(x):

	j3 = 1
	c9 = 9
	paths = []
	try:
		if j3 <= 6:
			c9 = 4/c9
			paths.append(1)
		else:
			j3 = x-8
			j3 = j3+j3
			paths.append(2)
		if x > 2:
			x = c9/x
			j3 = j3/x
			x = 6-x
			paths.append(3)
		else:
			x = x/4
			j3 = j3*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))