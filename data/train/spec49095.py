import numpy as np 

def function(x):

	b0 = 5
	u1 = 5
	paths = []
	try:
		if u1 >= 0:
			x = x+3
			b0 = b0-u1
			u1 = 4+u1
			paths.append(1)
		else:
			u1 = 2-u1
			b0 = b0+x
			paths.append(2)
		if b0 <= 9:
			u1 = u1*5
			x = x-b0
			paths.append(3)
		else:
			x = x+b0
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