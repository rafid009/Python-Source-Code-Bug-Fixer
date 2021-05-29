import numpy as np 

def function(x):

	b0 = 2
	r0 = 7
	paths = []
	try:
		if b0 > 7:
			r0 = 5/b0
			paths.append(1)
		else:
			b0 = r0+2
			b0 = 2-3
			paths.append(2)
		if b0 > 2:
			x = 5*x
			paths.append(3)
		else:
			x = x*r0
			x = b0/x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))