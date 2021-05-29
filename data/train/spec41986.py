import numpy as np 

def function(x):

	r8 = x
	b9 = x
	paths = []
	try:
		if r8 < 6:
			r8 = r8/8
			x = x+5
			r8 = x+r8
			paths.append(1)
		else:
			r8 = b9+r8
			paths.append(2)
		if b9 >= 8:
			r8 = 8*r8
			b9 = 8*1
			r8 = r8*1
			paths.append(3)
		else:
			x = 3+r8
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