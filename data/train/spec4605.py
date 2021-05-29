import numpy as np 

def function(x):

	t1 = 7
	e2 = x
	x = 0
	paths = []
	try:
		if e2 < 5:
			x = x-0
			paths.append(1)
		else:
			e2 = e2/e2
			e2 = 7*7
			paths.append(2)
		if e2 >= 6:
			e2 = 9/6
			t1 = t1/e2
			paths.append(3)
		else:
			x = t1/t1
			x = x/x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))