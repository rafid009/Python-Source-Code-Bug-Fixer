import numpy as np 

def function(x):

	i4 = 3
	u2 = x
	paths = []
	try:
		if u2 >= 7:
			x = x/x
			u2 = u2*u2
			paths.append(1)
		else:
			u2 = u2/1
			x = x*9
			u2 = 4-u2
			paths.append(2)
		if u2 <= 1:
			i4 = i4/6
			paths.append(3)
		else:
			i4 = i4-0
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