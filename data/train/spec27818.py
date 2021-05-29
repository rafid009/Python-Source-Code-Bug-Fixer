import numpy as np 

def function(x):

	b9 = x
	r8 = 3
	paths = []
	try:
		if x <= 2:
			x = 0-x
			x = 4/r8
			b9 = x*r8
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if r8 < 9:
			r8 = 7+r8
			r8 = r8+2
			paths.append(3)
		else:
			b9 = 0+b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))