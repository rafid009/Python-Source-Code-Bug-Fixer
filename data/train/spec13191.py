import numpy as np 

def function(x):

	t6 = 5
	e0 = 8
	x = x
	paths = []
	try:
		if t6 >= 7:
			x = x+2
			paths.append(1)
		else:
			t6 = 1+t6
			t6 = 5-6
			e0 = 7*4
			paths.append(2)
		if x >= 7:
			x = x-2
			t6 = t6*t6
			e0 = e0/5
			paths.append(3)
		else:
			x = t6-6
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))