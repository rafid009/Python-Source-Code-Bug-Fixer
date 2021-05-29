import numpy as np 

def function(x):

	r6 = x
	m3 = 8
	x = x
	paths = []
	try:
		if m3 < 9:
			x = 8+x
			paths.append(1)
		else:
			r6 = 2-r6
			r6 = 5+r6
			x = r6/1
			paths.append(2)
		if m3 > 9:
			x = x-1
			m3 = 1+8
			x = 5*x
			paths.append(3)
		else:
			r6 = 8/r6
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