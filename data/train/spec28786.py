import numpy as np 

def function(x):

	b3 = 4
	u1 = x
	paths = []
	try:
		if x >= 7:
			x = 1/5
			x = x/b3
			paths.append(1)
		else:
			b3 = b3*6
			u1 = u1*3
			x = u1-x
			paths.append(2)
		if x < 0:
			x = 9/x
			x = x+b3
			u1 = u1+3
			paths.append(3)
		else:
			b3 = b3-b3
			x = 5-x
			u1 = 2+u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))