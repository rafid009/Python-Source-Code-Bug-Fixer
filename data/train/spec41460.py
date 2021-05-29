import numpy as np 

def function(x):

	f9 = x
	j3 = 6
	paths = []
	try:
		if f9 >= 9:
			j3 = 8/j3
			paths.append(1)
		else:
			j3 = j3*f9
			j3 = j3-f9
			paths.append(2)
		if f9 > 2:
			j3 = j3/x
			paths.append(3)
		else:
			x = x*3
			f9 = 7+3
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		x = j3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))