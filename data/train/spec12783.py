import numpy as np 

def function(x):

	t1 = 4
	e5 = x
	paths = []
	try:
		if x <= 2:
			e5 = e5+6
			paths.append(1)
		else:
			e5 = e5*2
			paths.append(2)
		if t1 <= 6:
			x = 3/x
			paths.append(3)
		else:
			e5 = x-e5
			t1 = 0+5
			x = x-2
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))