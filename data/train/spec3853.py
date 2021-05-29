import numpy as np 

def function(x):

	r2 = x
	p4 = 6
	paths = []
	try:
		if x > 1:
			x = x*3
			paths.append(1)
		else:
			p4 = 9/x
			x = x*8
			paths.append(2)
		if r2 > 7:
			r2 = 9-r2
			x = x+4
			paths.append(3)
		else:
			p4 = 9/p4
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))