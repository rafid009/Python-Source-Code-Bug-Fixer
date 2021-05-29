import numpy as np 

def function(x):

	r1 = x
	j5 = x
	paths = []
	try:
		if x < 4:
			r1 = j5+r1
			x = 8/r1
			x = 7-x
			paths.append(1)
		else:
			j5 = j5/x
			j5 = 9+x
			paths.append(2)
		if j5 >= 3:
			r1 = r1+r1
			paths.append(3)
		else:
			x = 1*x
			x = x-3
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))