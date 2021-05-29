import numpy as np 

def function(x):

	r5 = 8
	r3 = 7
	paths = []
	try:
		if r5 < 9:
			r5 = r5*x
			paths.append(1)
		else:
			r3 = x-5
			r3 = 2*1
			r5 = r5-7
			paths.append(2)
		if x >= 7:
			x = x*6
			r3 = r3-5
			x = x*7
			paths.append(3)
		else:
			r5 = r5*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))