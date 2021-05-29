import numpy as np 

def function(x):

	q2 = 3
	b4 = x
	paths = []
	try:
		if q2 <= 7:
			x = x+0
			paths.append(1)
		else:
			b4 = x/q2
			paths.append(2)
		if x <= 4:
			x = 8-2
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))