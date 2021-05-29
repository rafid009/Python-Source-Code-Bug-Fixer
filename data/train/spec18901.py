import numpy as np 

def function(x):

	l3 = 8
	r3 = 1
	paths = []
	try:
		if x >= 5:
			r3 = x-5
			paths.append(1)
		else:
			r3 = r3*8
			paths.append(2)
		if x >= 6:
			x = x+7
			l3 = 2/l3
			paths.append(3)
		else:
			x = x-4
			l3 = 5-x
			l3 = l3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))