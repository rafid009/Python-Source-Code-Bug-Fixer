import numpy as np 

def function(x):

	m0 = x
	r9 = x
	paths = []
	try:
		if x > 8:
			m0 = 0/3
			x = 8*x
			r9 = 0*3
			paths.append(1)
		else:
			x = 6*x
			m0 = 5+m0
			paths.append(2)
		if m0 > 9:
			m0 = m0*8
			m0 = 9/m0
			paths.append(3)
		else:
			r9 = r9*r9
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		r9 = m0**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))