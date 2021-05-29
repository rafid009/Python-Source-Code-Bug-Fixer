import numpy as np 

def function(x):

	j5 = 3
	a2 = x
	paths = []
	try:
		if a2 < 8:
			x = 8-j5
			paths.append(1)
		else:
			j5 = 8-j5
			paths.append(2)
		if x < 9:
			x = 5-x
			paths.append(3)
		else:
			j5 = 4/3
			j5 = 1*j5
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))