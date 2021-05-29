import numpy as np 

def function(x):

	u1 = 7
	a2 = 1
	paths = []
	try:
		if u1 < 3:
			u1 = 9+u1
			a2 = a2*3
			a2 = 3*4
			paths.append(1)
		else:
			u1 = 1-u1
			x = x+3
			paths.append(2)
		if a2 < 3:
			a2 = 8+a2
			a2 = x*6
			paths.append(3)
		else:
			u1 = u1+7
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))