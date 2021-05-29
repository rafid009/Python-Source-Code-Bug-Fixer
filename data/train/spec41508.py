import numpy as np 

def function(x):

	r0 = x
	j3 = x
	x = 4
	paths = []
	try:
		if r0 < 2:
			r0 = x-r0
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x <= 9:
			j3 = j3*r0
			x = x-j3
			paths.append(3)
		else:
			j3 = x*j3
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