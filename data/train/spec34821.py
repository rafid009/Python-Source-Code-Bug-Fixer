import numpy as np 

def function(x):

	e5 = 1
	r0 = x
	paths = []
	try:
		if x < 9:
			r0 = 7*7
			e5 = 7+x
			paths.append(1)
		else:
			x = e5+x
			e5 = 1-8
			x = x-e5
			paths.append(2)
		if r0 > 4:
			x = x-9
			e5 = r0/4
			x = 1/x
			paths.append(3)
		else:
			r0 = r0*0
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