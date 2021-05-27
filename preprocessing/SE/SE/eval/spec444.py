import numpy as np 

def function(x):

	a1 = 3
	t2 = 1
	paths = []
	try:
		if x >= 7:
			a1 = 9/t2
			x = 2-x
			paths.append(1)
		else:
			t2 = 7-x
			paths.append(2)
		if a1 <= 1:
			t2 = 5-a1
			x = 9*x
			paths.append(3)
		else:
			x = x*t2
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