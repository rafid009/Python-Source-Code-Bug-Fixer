import numpy as np 

def function(x):

	e2 = x
	t2 = 8
	paths = []
	try:
		if e2 > 1:
			e2 = 5-e2
			t2 = t2/3
			paths.append(1)
		else:
			t2 = 4-7
			x = 7/e2
			x = e2/x
			paths.append(2)
		if t2 < 3:
			e2 = 9+e2
			e2 = e2-6
			t2 = 9*t2
			paths.append(3)
		else:
			e2 = e2-9
			x = x*7
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))