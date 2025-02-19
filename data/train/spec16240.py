import numpy as np 

def function(x):

	j7 = 2
	b7 = x
	paths = []
	try:
		if j7 > 6:
			x = j7/b7
			paths.append(1)
		else:
			x = x*b7
			j7 = x-j7
			j7 = x/5
			paths.append(2)
		if j7 >= 3:
			j7 = x/6
			paths.append(3)
		else:
			j7 = x*7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		j7 = b7**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))