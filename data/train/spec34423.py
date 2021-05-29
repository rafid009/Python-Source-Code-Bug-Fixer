import numpy as np 

def function(x):

	u1 = x
	x9 = 6
	paths = []
	try:
		if x9 <= 6:
			x9 = x*x9
			x = 3+3
			paths.append(1)
		else:
			x9 = 6+x9
			x = 1/x
			paths.append(2)
		if x9 > 4:
			x9 = 5+x9
			x9 = 4+5
			u1 = u1+1
			paths.append(3)
		else:
			x = u1/x
			x = x+3
			x9 = 4-5
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