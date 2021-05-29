import numpy as np 

def function(x):

	q4 = 7
	t8 = x
	paths = []
	try:
		if t8 <= 4:
			q4 = q4*q4
			t8 = 1+t8
			q4 = 9-2
			paths.append(1)
		else:
			x = x-t8
			x = 1+x
			q4 = 0/8
			paths.append(2)
		if t8 <= 0:
			t8 = t8/7
			t8 = t8+4
			paths.append(3)
		else:
			x = 0/x
			x = 8-3
			x = x*6
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