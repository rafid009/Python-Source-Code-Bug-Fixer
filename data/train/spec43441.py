import numpy as np 

def function(x):

	o5 = 2
	u2 = x
	x = 0
	paths = []
	try:
		if o5 < 0:
			u2 = 3+u2
			o5 = o5*3
			paths.append(1)
		else:
			o5 = o5-7
			paths.append(2)
		if u2 < 5:
			o5 = o5/o5
			paths.append(3)
		else:
			x = 5+o5
			u2 = x/6
			u2 = 1+u2
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