import numpy as np 

def function(x):

	o0 = 6
	m6 = x
	paths = []
	try:
		if o0 < 5:
			o0 = o0*4
			paths.append(1)
		else:
			m6 = x*m6
			m6 = m6+o0
			m6 = m6*4
			paths.append(2)
		if m6 > 1:
			m6 = m6*x
			paths.append(3)
		else:
			o0 = o0-m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o0 = x**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))