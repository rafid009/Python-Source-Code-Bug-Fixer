import numpy as np 

def function(x):

	u2 = x
	p9 = 9
	paths = []
	try:
		if u2 < 2:
			x = x-9
			p9 = p9*x
			x = x-p9
			paths.append(1)
		else:
			u2 = u2+5
			paths.append(2)
		if x > 5:
			x = p9-u2
			paths.append(3)
		else:
			u2 = 4*u2
			p9 = p9/x
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