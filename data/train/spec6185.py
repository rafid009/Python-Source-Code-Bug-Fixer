import numpy as np 

def function(x):

	r1 = x
	e2 = 7
	x = 2
	paths = []
	try:
		if r1 >= 6:
			e2 = x-e2
			paths.append(1)
		else:
			r1 = r1+6
			e2 = r1+e2
			e2 = e2-5
			paths.append(2)
		if x > 6:
			r1 = 3-r1
			paths.append(3)
		else:
			x = r1+3
			e2 = e2/7
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))