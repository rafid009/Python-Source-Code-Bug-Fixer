import numpy as np 

def function(x):

	t7 = x
	q6 = 8
	x = x
	paths = []
	try:
		if q6 > 2:
			t7 = 7/x
			paths.append(1)
		else:
			t7 = 2/2
			t7 = t7*2
			x = x*q6
			paths.append(2)
		if q6 > 8:
			t7 = 5+2
			x = x/2
			paths.append(3)
		else:
			t7 = x*8
			t7 = t7-q6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))