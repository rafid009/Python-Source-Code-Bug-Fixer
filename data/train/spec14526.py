import numpy as np 

def function(x):

	t2 = 1
	e9 = 1
	paths = []
	try:
		if e9 <= 3:
			t2 = e9*e9
			paths.append(1)
		else:
			t2 = x*1
			t2 = t2*1
			e9 = e9-x
			paths.append(2)
		if t2 >= 2:
			t2 = t2*7
			paths.append(3)
		else:
			x = x/x
			e9 = e9/1
			x = x-3
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