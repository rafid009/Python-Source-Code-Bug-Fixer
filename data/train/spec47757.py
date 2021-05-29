import numpy as np 

def function(x):

	u1 = x
	b4 = 2
	paths = []
	try:
		if x < 6:
			x = x*b4
			paths.append(1)
		else:
			x = x/b4
			paths.append(2)
		if b4 > 6:
			x = x+x
			u1 = x-8
			paths.append(3)
		else:
			u1 = 6*x
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))