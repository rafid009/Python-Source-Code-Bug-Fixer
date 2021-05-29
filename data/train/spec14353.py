import numpy as np 

def function(x):

	u2 = 1
	l3 = x
	paths = []
	try:
		if l3 >= 6:
			l3 = l3/8
			u2 = x+4
			paths.append(1)
		else:
			u2 = 3*4
			u2 = u2-x
			u2 = u2/1
			paths.append(2)
		if l3 < 8:
			l3 = 7*1
			u2 = u2-4
			paths.append(3)
		else:
			l3 = 5*u2
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