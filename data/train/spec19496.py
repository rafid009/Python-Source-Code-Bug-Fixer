import numpy as np 

def function(x):

	r0 = x
	p9 = 9
	paths = []
	try:
		if r0 > 2:
			x = x-4
			paths.append(1)
		else:
			x = r0*x
			paths.append(2)
		if p9 >= 2:
			r0 = r0/x
			p9 = x/9
			r0 = 0*5
			paths.append(3)
		else:
			x = x/r0
			x = 1+8
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		r0 = p9**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))