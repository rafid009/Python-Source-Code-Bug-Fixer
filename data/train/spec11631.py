import numpy as np 

def function(x):

	r0 = x
	e5 = x
	paths = []
	try:
		if r0 >= 9:
			r0 = 1*4
			e5 = e5-r0
			e5 = r0/5
			paths.append(1)
		else:
			r0 = x*x
			r0 = r0*r0
			r0 = 9-r0
			paths.append(2)
		if e5 > 5:
			e5 = x*9
			r0 = r0*x
			x = 1+x
			paths.append(3)
		else:
			e5 = e5-4
			x = x+x
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))