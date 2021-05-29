import numpy as np 

def function(x):

	v6 = 9
	j5 = x
	paths = []
	try:
		if x > 8:
			j5 = 2*j5
			j5 = j5-3
			paths.append(1)
		else:
			j5 = 9*1
			paths.append(2)
		if v6 >= 0:
			j5 = 0-v6
			j5 = 8-j5
			paths.append(3)
		else:
			j5 = 7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))