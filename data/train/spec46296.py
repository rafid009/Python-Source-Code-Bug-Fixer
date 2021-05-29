import numpy as np 

def function(x):

	b0 = x
	r6 = 7
	paths = []
	try:
		if x >= 3:
			r6 = r6/x
			b0 = 3/b0
			r6 = 5/5
			paths.append(1)
		else:
			r6 = 8*b0
			paths.append(2)
		if r6 < 1:
			b0 = 7-b0
			x = x*5
			x = x/1
			paths.append(3)
		else:
			b0 = b0*0
			x = r6-7
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