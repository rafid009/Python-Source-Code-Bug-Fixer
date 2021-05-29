import numpy as np 

def function(x):

	l9 = x
	v3 = x
	paths = []
	try:
		if x >= 9:
			v3 = v3-4
			l9 = l9-4
			paths.append(1)
		else:
			l9 = l9-1
			x = x+5
			paths.append(2)
		if l9 >= 6:
			l9 = l9-7
			paths.append(3)
		else:
			v3 = v3/v3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))