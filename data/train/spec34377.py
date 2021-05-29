import numpy as np 

def function(x):

	j3 = 7
	l4 = x
	x = 4
	paths = []
	try:
		if j3 >= 5:
			j3 = 7/j3
			l4 = l4-0
			paths.append(1)
		else:
			j3 = l4*j3
			l4 = 6/j3
			paths.append(2)
		if j3 <= 6:
			x = 9-8
			paths.append(3)
		else:
			j3 = j3-4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))