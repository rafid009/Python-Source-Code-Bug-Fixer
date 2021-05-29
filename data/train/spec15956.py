import numpy as np 

def function(x):

	j5 = x
	x8 = 2
	paths = []
	try:
		if x >= 2:
			x = 4-4
			paths.append(1)
		else:
			x8 = j5/x8
			x8 = x+j5
			paths.append(2)
		if x8 <= 3:
			j5 = j5+j5
			paths.append(3)
		else:
			j5 = x8+j5
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		j5 = x8**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))