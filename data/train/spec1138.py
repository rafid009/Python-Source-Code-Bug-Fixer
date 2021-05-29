import numpy as np 

def function(x):

	a3 = x
	u1 = 5
	paths = []
	try:
		if u1 < 3:
			a3 = u1-x
			x = x-a3
			u1 = 2+u1
			paths.append(1)
		else:
			u1 = u1-u1
			u1 = 4+u1
			paths.append(2)
		if a3 >= 0:
			a3 = u1+x
			a3 = a3/3
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		a3 = a3**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))