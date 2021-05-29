import numpy as np 

def function(x):

	p9 = x
	r2 = x
	paths = []
	try:
		if x >= 3:
			p9 = p9-3
			x = 1*3
			paths.append(1)
		else:
			x = x-r2
			paths.append(2)
		if p9 < 6:
			p9 = 8-6
			p9 = 8/2
			r2 = 2/5
			paths.append(3)
		else:
			r2 = 9-r2
			x = r2-x
			p9 = 1*p9
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