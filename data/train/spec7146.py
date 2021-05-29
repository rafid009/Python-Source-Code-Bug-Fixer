import numpy as np 

def function(x):

	b0 = 0
	r0 = x
	paths = []
	try:
		if r0 > 5:
			b0 = r0-b0
			paths.append(1)
		else:
			b0 = 1/r0
			r0 = r0/b0
			x = b0/5
			paths.append(2)
		if b0 >= 7:
			r0 = 3-r0
			paths.append(3)
		else:
			r0 = 6-b0
			x = 8*b0
			r0 = r0*2
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))