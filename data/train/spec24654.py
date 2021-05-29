import numpy as np 

def function(x):

	e2 = x
	u1 = 5
	paths = []
	try:
		if u1 <= 3:
			u1 = 1+u1
			u1 = e2/6
			x = 6*x
			paths.append(1)
		else:
			x = 2+2
			e2 = 2-e2
			x = x-9
			paths.append(2)
		if u1 >= 0:
			u1 = u1/u1
			paths.append(3)
		else:
			u1 = u1+4
			x = e2-e2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		u1 = e2**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))