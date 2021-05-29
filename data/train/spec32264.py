import numpy as np 

def function(x):

	j3 = x
	l4 = x
	paths = []
	try:
		if l4 <= 9:
			j3 = x/j3
			paths.append(1)
		else:
			x = 8-l4
			x = x+j3
			paths.append(2)
		if j3 <= 3:
			x = x/7
			paths.append(3)
		else:
			x = x/j3
			j3 = j3/1
			x = x-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))