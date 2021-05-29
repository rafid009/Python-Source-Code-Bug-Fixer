import numpy as np 

def function(x):

	b9 = x
	r0 = 3
	x = x
	paths = []
	try:
		if r0 < 9:
			r0 = 8+3
			r0 = r0/9
			b9 = 9*b9
			paths.append(1)
		else:
			r0 = 5*r0
			b9 = 3/b9
			paths.append(2)
		if r0 < 0:
			b9 = x+b9
			paths.append(3)
		else:
			r0 = r0+1
			b9 = 9*b9
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