import numpy as np 

def function(x):

	j9 = x
	j7 = x
	paths = []
	try:
		if j7 <= 2:
			x = x-2
			j7 = j7-8
			paths.append(1)
		else:
			x = 0*8
			x = x/8
			paths.append(2)
		if x >= 5:
			j7 = j7/x
			paths.append(3)
		else:
			j7 = 2/j7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		j7 = j7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))