import numpy as np 

def function(x):

	q4 = 6
	t2 = 5
	paths = []
	try:
		if t2 >= 8:
			x = x+3
			q4 = q4-3
			paths.append(1)
		else:
			t2 = 8-t2
			paths.append(2)
		if t2 <= 7:
			t2 = 0-t2
			paths.append(3)
		else:
			t2 = x-1
			q4 = 1/q4
			q4 = q4+q4
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