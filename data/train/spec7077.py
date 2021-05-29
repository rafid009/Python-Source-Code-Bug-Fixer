import numpy as np 

def function(x):

	x5 = x
	r0 = 2
	x = 9
	paths = []
	try:
		if x > 0:
			r0 = x*1
			x5 = 9*x5
			paths.append(1)
		else:
			r0 = r0*3
			paths.append(2)
		if x5 < 8:
			x = x*8
			x = x/5
			r0 = x+6
			paths.append(3)
		else:
			r0 = r0*2
			r0 = r0-5
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))