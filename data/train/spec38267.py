import numpy as np 

def function(x):

	o7 = x
	m0 = x
	paths = []
	try:
		if m0 >= 6:
			x = x*7
			o7 = 3*o7
			x = 2+6
			paths.append(1)
		else:
			m0 = m0*8
			m0 = 5*m0
			m0 = m0*1
			paths.append(2)
		if o7 <= 7:
			x = 3-6
			paths.append(3)
		else:
			x = 0/o7
			m0 = m0+0
			m0 = m0*4
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		m0 = o7**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))