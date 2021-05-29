import numpy as np 

def function(x):

	b9 = x
	r0 = x
	paths = []
	try:
		if b9 < 2:
			x = 3/x
			b9 = x/x
			paths.append(1)
		else:
			x = 1+2
			paths.append(2)
		if b9 > 7:
			r0 = r0+0
			x = 2*9
			b9 = b9/8
			paths.append(3)
		else:
			b9 = 2*x
			b9 = b9/3
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))