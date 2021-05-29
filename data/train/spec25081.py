import numpy as np 

def function(x):

	t7 = x
	q8 = x
	paths = []
	try:
		if t7 > 1:
			q8 = q8+3
			paths.append(1)
		else:
			t7 = 6*t7
			x = x*4
			paths.append(2)
		if q8 > 2:
			x = 4*x
			q8 = 2+3
			paths.append(3)
		else:
			x = 0*6
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))