import numpy as np 

def function(x):

	r0 = x
	p6 = x
	paths = []
	try:
		if p6 > 6:
			r0 = 9-r0
			x = x-4
			paths.append(1)
		else:
			x = p6+5
			x = 1/x
			paths.append(2)
		if r0 <= 7:
			r0 = x-9
			p6 = r0-x
			paths.append(3)
		else:
			r0 = 0*x
			p6 = p6-2
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		r0 = p6**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))