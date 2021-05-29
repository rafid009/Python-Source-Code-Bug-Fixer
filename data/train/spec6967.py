import numpy as np 

def function(x):

	r5 = 7
	f5 = 7
	paths = []
	try:
		if r5 <= 6:
			x = 0*x
			x = 9/x
			x = x/5
			paths.append(1)
		else:
			f5 = 9*0
			f5 = f5/6
			r5 = r5*x
			paths.append(2)
		if f5 <= 8:
			x = x-f5
			paths.append(3)
		else:
			f5 = f5/x
			r5 = r5+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))