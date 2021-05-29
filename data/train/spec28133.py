import numpy as np 

def function(x):

	b0 = 0
	r2 = x
	x = 1
	paths = []
	try:
		if b0 >= 3:
			x = x+b0
			paths.append(1)
		else:
			r2 = r2/5
			x = x-5
			paths.append(2)
		if r2 >= 8:
			r2 = r2/x
			r2 = 4/r2
			paths.append(3)
		else:
			b0 = r2+3
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		x = r2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))