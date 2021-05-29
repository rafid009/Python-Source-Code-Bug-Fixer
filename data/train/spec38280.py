import numpy as np 

def function(x):

	u1 = 5
	x5 = 3
	x = x
	paths = []
	try:
		if u1 <= 2:
			u1 = u1+3
			x = x/8
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x > 0:
			u1 = 4+8
			x5 = 3*x5
			x5 = 0-x5
			paths.append(3)
		else:
			u1 = u1+u1
			u1 = u1+1
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))