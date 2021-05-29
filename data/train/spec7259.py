import numpy as np 

def function(x):

	e2 = x
	r6 = 0
	paths = []
	try:
		if r6 < 0:
			r6 = 1-r6
			e2 = e2/e2
			paths.append(1)
		else:
			r6 = e2-9
			paths.append(2)
		if e2 < 7:
			x = x-e2
			paths.append(3)
		else:
			r6 = r6+r6
			e2 = e2+1
			x = x*r6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r6 = x**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))