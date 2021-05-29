import numpy as np 

def function(x):

	q4 = 7
	b6 = x
	paths = []
	try:
		if b6 <= 1:
			x = x+q4
			q4 = q4/q4
			paths.append(1)
		else:
			q4 = 0-q4
			x = 5-b6
			b6 = 4/5
			paths.append(2)
		if q4 >= 3:
			b6 = b6+b6
			paths.append(3)
		else:
			q4 = 2-5
			q4 = b6*3
			q4 = 8/x
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