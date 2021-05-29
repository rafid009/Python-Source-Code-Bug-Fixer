import numpy as np 

def function(x):

	m9 = 4
	r2 = x
	x = x
	paths = []
	try:
		if x <= 0:
			m9 = m9/3
			paths.append(1)
		else:
			x = 3*m9
			m9 = 3/2
			paths.append(2)
		if m9 > 9:
			x = x*8
			r2 = r2-2
			m9 = m9-m9
			paths.append(3)
		else:
			m9 = r2*m9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))