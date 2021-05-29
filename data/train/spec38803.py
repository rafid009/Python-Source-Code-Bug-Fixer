import numpy as np 

def function(x):

	d0 = 3
	m0 = 5
	paths = []
	try:
		if x > 8:
			m0 = m0/3
			x = d0/9
			paths.append(1)
		else:
			x = 0-x
			m0 = m0-4
			d0 = d0/x
			paths.append(2)
		if d0 >= 4:
			m0 = m0+x
			m0 = m0+9
			paths.append(3)
		else:
			m0 = m0*m0
			m0 = m0+3
			m0 = 4+m0
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))