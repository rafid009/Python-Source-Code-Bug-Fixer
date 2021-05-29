import numpy as np 

def function(x):

	j7 = x
	y6 = 1
	x = 6
	paths = []
	try:
		if x > 6:
			x = x+5
			j7 = j7+1
			paths.append(1)
		else:
			j7 = 4*j7
			j7 = 6+y6
			j7 = 3-2
			paths.append(2)
		if x < 8:
			x = x+y6
			j7 = j7-2
			paths.append(3)
		else:
			x = j7/9
			x = 3*y6
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))