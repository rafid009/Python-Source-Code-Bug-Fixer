import numpy as np 

def function(x):

	m0 = x
	r2 = 7
	paths = []
	try:
		if x > 4:
			r2 = r2+4
			x = x+x
			paths.append(1)
		else:
			r2 = x+x
			x = 5+9
			paths.append(2)
		if x >= 5:
			m0 = 8*3
			paths.append(3)
		else:
			r2 = 2/r2
			r2 = r2+6
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