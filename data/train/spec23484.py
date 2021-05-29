import numpy as np 

def function(x):

	u2 = x
	e6 = x
	paths = []
	try:
		if e6 <= 8:
			u2 = 5-u2
			x = 5*x
			paths.append(1)
		else:
			x = e6/x
			u2 = u2+e6
			u2 = u2/9
			paths.append(2)
		if u2 > 2:
			e6 = 1-4
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))