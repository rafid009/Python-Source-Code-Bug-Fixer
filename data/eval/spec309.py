import numpy as np 

def function(x):

	u1 = 5
	n3 = 7
	x = 9
	paths = []
	try:
		if x < 8:
			x = n3-n3
			paths.append(1)
		else:
			u1 = 3/x
			x = u1*8
			u1 = u1+n3
			paths.append(2)
		if n3 <= 6:
			x = x+2
			paths.append(3)
		else:
			x = u1/x
			x = 4-5
			n3 = n3-2
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