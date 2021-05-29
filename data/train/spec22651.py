import numpy as np 

def function(x):

	i3 = 7
	q4 = 1
	paths = []
	try:
		if i3 < 4:
			x = x-6
			paths.append(1)
		else:
			i3 = x/6
			i3 = i3*x
			paths.append(2)
		if x >= 6:
			q4 = 4+8
			paths.append(3)
		else:
			q4 = 2/q4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))