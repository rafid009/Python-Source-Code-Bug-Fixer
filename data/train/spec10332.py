import numpy as np 

def function(x):

	m0 = x
	r2 = 7
	paths = []
	try:
		if m0 <= 6:
			r2 = r2+r2
			r2 = r2/6
			paths.append(1)
		else:
			m0 = m0/9
			paths.append(2)
		if x > 2:
			x = 2*x
			m0 = 9-6
			paths.append(3)
		else:
			r2 = m0/1
			r2 = r2-7
			x = 7+x
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