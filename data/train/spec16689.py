import numpy as np 

def function(x):

	m0 = x
	r9 = 6
	x = x
	paths = []
	try:
		if r9 <= 4:
			m0 = 4*x
			r9 = 1+r9
			paths.append(1)
		else:
			r9 = m0+2
			m0 = m0+9
			paths.append(2)
		if r9 > 2:
			m0 = m0*6
			x = 5/r9
			paths.append(3)
		else:
			x = m0-x
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))