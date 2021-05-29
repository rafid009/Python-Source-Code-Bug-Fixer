import numpy as np 

def function(x):

	k2 = x
	l3 = x
	paths = []
	try:
		if x > 6:
			x = k2*x
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if k2 >= 0:
			k2 = 8*1
			x = x/7
			paths.append(3)
		else:
			x = x*8
			x = x/x
			x = 4/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))