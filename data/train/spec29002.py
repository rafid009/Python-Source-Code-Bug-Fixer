import numpy as np 

def function(x):

	t8 = x
	r0 = x
	paths = []
	try:
		if t8 < 1:
			r0 = r0/t8
			r0 = 6*r0
			x = x+4
			paths.append(1)
		else:
			r0 = 9*r0
			x = x+0
			paths.append(2)
		if r0 < 1:
			r0 = 4*2
			r0 = x*4
			paths.append(3)
		else:
			x = x/1
			r0 = r0+t8
			r0 = x/2
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