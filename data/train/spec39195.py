import numpy as np 

def function(x):

	b2 = x
	u2 = 6
	x = x
	paths = []
	try:
		if u2 < 5:
			u2 = u2*b2
			x = x*x
			paths.append(1)
		else:
			u2 = u2/6
			u2 = 3+u2
			paths.append(2)
		if b2 < 9:
			x = x*8
			x = x*u2
			u2 = u2-7
			paths.append(3)
		else:
			u2 = u2/7
			b2 = 3/8
			b2 = 7/x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))