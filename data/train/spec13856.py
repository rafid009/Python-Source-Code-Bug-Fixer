import numpy as np 

def function(x):

	f9 = 6
	j5 = x
	paths = []
	try:
		if x > 6:
			j5 = j5*f9
			j5 = 3/2
			x = x+j5
			paths.append(1)
		else:
			f9 = 7/f9
			j5 = j5*5
			paths.append(2)
		if x > 0:
			f9 = f9*j5
			f9 = f9+8
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		j5 = j5**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))