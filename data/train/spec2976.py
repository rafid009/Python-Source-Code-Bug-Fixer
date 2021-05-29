import numpy as np 

def function(x):

	j3 = 5
	a6 = 3
	paths = []
	try:
		if x > 3:
			x = x/6
			j3 = 1+a6
			paths.append(1)
		else:
			j3 = j3+j3
			paths.append(2)
		if x >= 1:
			a6 = a6/1
			a6 = j3-8
			j3 = a6/j3
			paths.append(3)
		else:
			x = x/1
			j3 = j3/1
			x = 6/x
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