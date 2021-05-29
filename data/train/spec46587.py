import numpy as np 

def function(x):

	r0 = 0
	x6 = 1
	paths = []
	try:
		if x > 4:
			x6 = 2+3
			x6 = 4-1
			paths.append(1)
		else:
			x6 = x6+x
			paths.append(2)
		if x <= 2:
			x = x+4
			r0 = r0/x
			paths.append(3)
		else:
			x = x/3
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))