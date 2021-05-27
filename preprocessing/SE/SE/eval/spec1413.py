import numpy as np 

def function(x):

	j7 = x
	k7 = x
	x = x
	paths = []
	try:
		if x <= 2:
			j7 = 1-j7
			j7 = j7+5
			paths.append(1)
		else:
			x = x/9
			j7 = j7/j7
			paths.append(2)
		if k7 > 5:
			j7 = j7-k7
			x = 1-1
			paths.append(3)
		else:
			j7 = 7+j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))