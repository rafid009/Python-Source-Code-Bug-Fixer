import numpy as np 

def function(x):

	q3 = 2
	t8 = 0
	paths = []
	try:
		if q3 >= 1:
			t8 = x+t8
			paths.append(1)
		else:
			t8 = x+t8
			paths.append(2)
		if t8 <= 4:
			q3 = 5-q3
			q3 = 1*8
			paths.append(3)
		else:
			x = x/4
			t8 = t8/q3
			t8 = x/4
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