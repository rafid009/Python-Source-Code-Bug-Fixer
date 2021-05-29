import numpy as np 

def function(x):

	t8 = x
	q0 = 2
	paths = []
	try:
		if q0 > 9:
			q0 = 2-t8
			t8 = 6+t8
			paths.append(1)
		else:
			q0 = 6-q0
			t8 = 4/8
			q0 = 3*q0
			paths.append(2)
		if q0 >= 6:
			t8 = 9+t8
			t8 = t8*1
			paths.append(3)
		else:
			q0 = q0*x
			t8 = t8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))