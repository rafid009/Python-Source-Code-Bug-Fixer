import numpy as np 

def function(x):

	n7 = x
	u1 = x
	paths = []
	try:
		if n7 < 7:
			x = x-7
			paths.append(1)
		else:
			n7 = x*0
			x = 6+x
			x = x-8
			paths.append(2)
		if n7 >= 0:
			u1 = 2/u1
			paths.append(3)
		else:
			n7 = u1+x
			u1 = 2*u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))