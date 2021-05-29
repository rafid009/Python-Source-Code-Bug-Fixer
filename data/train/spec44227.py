import numpy as np 

def function(x):

	a7 = x
	r0 = 0
	paths = []
	try:
		if r0 <= 2:
			a7 = a7*1
			a7 = a7*x
			r0 = x*7
			paths.append(1)
		else:
			a7 = r0+1
			x = 8-x
			x = x-6
			paths.append(2)
		if r0 > 7:
			x = a7+x
			paths.append(3)
		else:
			r0 = r0+a7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r0 = x**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))