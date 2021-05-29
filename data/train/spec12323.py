import numpy as np 

def function(x):

	e2 = 3
	j2 = 1
	paths = []
	try:
		if j2 > 5:
			x = x-4
			paths.append(1)
		else:
			j2 = j2*9
			j2 = 8/j2
			paths.append(2)
		if x <= 8:
			j2 = j2*3
			x = j2*3
			paths.append(3)
		else:
			j2 = 0-j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		e2 = j2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))