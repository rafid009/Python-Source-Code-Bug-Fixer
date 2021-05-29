import numpy as np 

def function(x):

	t2 = 2
	q8 = 7
	paths = []
	try:
		if q8 >= 1:
			t2 = x+x
			x = x*q8
			paths.append(1)
		else:
			q8 = t2+t2
			paths.append(2)
		if q8 > 0:
			q8 = x-q8
			x = 7-x
			paths.append(3)
		else:
			q8 = x*q8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))