import numpy as np 

def function(x):

	a8 = 9
	j5 = 8
	paths = []
	try:
		if a8 < 8:
			x = x-5
			paths.append(1)
		else:
			j5 = x*6
			paths.append(2)
		if x < 3:
			x = x+6
			a8 = a8-6
			paths.append(3)
		else:
			x = j5/x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		a8 = j5**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))