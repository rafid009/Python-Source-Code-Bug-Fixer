import numpy as np 

def function(x):

	f2 = 0
	q7 = x
	paths = []
	try:
		if f2 >= 7:
			f2 = f2*2
			paths.append(1)
		else:
			f2 = f2/1
			q7 = x+3
			paths.append(2)
		if q7 > 2:
			f2 = f2*f2
			q7 = 6/q7
			q7 = x/q7
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))