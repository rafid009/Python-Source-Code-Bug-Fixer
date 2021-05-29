import numpy as np 

def function(x):

	t8 = 6
	q7 = 3
	paths = []
	try:
		if q7 <= 1:
			x = x-x
			t8 = 0/q7
			paths.append(1)
		else:
			q7 = x/7
			paths.append(2)
		if t8 >= 4:
			q7 = x+q7
			x = 1-x
			q7 = q7/x
			paths.append(3)
		else:
			q7 = q7*4
			t8 = 9+t8
			q7 = x*3
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