import numpy as np 

def function(x):

	d6 = x
	u2 = 7
	paths = []
	try:
		if d6 < 6:
			x = u2/6
			u2 = u2+3
			u2 = x+u2
			paths.append(1)
		else:
			x = x/4
			x = 9*d6
			paths.append(2)
		if d6 <= 7:
			d6 = 0+d6
			u2 = u2*d6
			paths.append(3)
		else:
			u2 = 2/u2
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