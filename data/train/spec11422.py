import numpy as np 

def function(x):

	a9 = 4
	u1 = x
	paths = []
	try:
		if u1 <= 5:
			a9 = a9*5
			paths.append(1)
		else:
			u1 = 9/u1
			paths.append(2)
		if u1 > 3:
			a9 = 9-x
			u1 = 8*4
			paths.append(3)
		else:
			a9 = u1/a9
			a9 = a9-2
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		a9 = u1**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))