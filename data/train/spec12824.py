import numpy as np 

def function(x):

	m0 = 4
	r5 = 5
	paths = []
	try:
		if x > 6:
			r5 = 1-x
			m0 = r5*2
			paths.append(1)
		else:
			m0 = m0*3
			x = x+m0
			x = x-x
			paths.append(2)
		if x > 2:
			x = 6*x
			paths.append(3)
		else:
			r5 = r5*3
			x = 9-x
			r5 = r5/1
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))