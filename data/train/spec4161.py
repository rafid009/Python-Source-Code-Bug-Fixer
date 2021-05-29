import numpy as np 

def function(x):

	t8 = 8
	q0 = x
	paths = []
	try:
		if q0 <= 2:
			t8 = 1/5
			q0 = t8-2
			t8 = 6+t8
			paths.append(1)
		else:
			t8 = q0-t8
			paths.append(2)
		if x <= 2:
			q0 = 9+q0
			t8 = 8*5
			q0 = 5+5
			paths.append(3)
		else:
			x = q0+t8
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		x = t8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))