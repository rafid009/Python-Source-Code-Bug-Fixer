import numpy as np 

def function(x):

	q6 = x
	v7 = x
	paths = []
	try:
		if v7 >= 9:
			v7 = 8/x
			paths.append(1)
		else:
			v7 = v7/5
			paths.append(2)
		if x >= 8:
			q6 = 2-q6
			paths.append(3)
		else:
			q6 = x+2
			q6 = q6+3
			v7 = v7-v7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))