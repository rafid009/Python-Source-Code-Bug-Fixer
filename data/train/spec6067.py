import numpy as np 

def function(x):

	r5 = x
	u2 = x
	paths = []
	try:
		if r5 > 6:
			r5 = 2-1
			u2 = 2*u2
			r5 = r5*3
			paths.append(1)
		else:
			u2 = u2+9
			u2 = 0+9
			r5 = r5+r5
			paths.append(2)
		if x <= 1:
			u2 = 4-u2
			r5 = 8*u2
			u2 = u2/x
			paths.append(3)
		else:
			r5 = r5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))