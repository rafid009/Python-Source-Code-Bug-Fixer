import numpy as np 

def function(x):

	x5 = 5
	j5 = 8
	paths = []
	try:
		if j5 > 3:
			j5 = j5/x
			x = x-4
			paths.append(1)
		else:
			j5 = x*4
			paths.append(2)
		if x5 > 4:
			x5 = j5*5
			x = 1/7
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x5 = j5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))