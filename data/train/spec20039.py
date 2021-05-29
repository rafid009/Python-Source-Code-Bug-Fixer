import numpy as np 

def function(x):

	m1 = 8
	r4 = x
	paths = []
	try:
		if r4 >= 0:
			r4 = r4-r4
			r4 = r4*x
			r4 = r4+x
			paths.append(1)
		else:
			m1 = m1+7
			x = x+r4
			paths.append(2)
		if m1 >= 0:
			x = 9-x
			x = 4+x
			paths.append(3)
		else:
			r4 = x+2
			x = x-2
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))