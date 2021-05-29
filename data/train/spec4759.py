import numpy as np 

def function(x):

	v8 = x
	q2 = 0
	paths = []
	try:
		if q2 <= 4:
			v8 = v8+q2
			paths.append(1)
		else:
			x = v8+2
			v8 = 5+2
			paths.append(2)
		if q2 < 6:
			x = q2-2
			v8 = v8-q2
			x = x-2
			paths.append(3)
		else:
			q2 = 2*8
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