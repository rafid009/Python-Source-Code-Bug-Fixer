import numpy as np 

def function(x):

	i7 = x
	r0 = 6
	x = 5
	paths = []
	try:
		if i7 <= 3:
			r0 = i7-i7
			i7 = 9/i7
			r0 = r0*r0
			paths.append(1)
		else:
			r0 = r0-i7
			x = r0-6
			paths.append(2)
		if i7 >= 9:
			x = r0/x
			x = x-7
			x = 0/8
			paths.append(3)
		else:
			r0 = x/4
			x = x+6
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