import numpy as np 

def function(x):

	q7 = x
	b6 = x
	paths = []
	try:
		if x >= 2:
			x = x*9
			paths.append(1)
		else:
			b6 = 3-b6
			paths.append(2)
		if q7 >= 3:
			q7 = q7-q7
			paths.append(3)
		else:
			b6 = 1+3
			b6 = 5/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))