import numpy as np 

def function(x):

	m4 = x
	k0 = x
	paths = []
	try:
		if k0 > 3:
			k0 = x*k0
			paths.append(1)
		else:
			k0 = k0*5
			k0 = 9/k0
			m4 = 8+m4
			paths.append(2)
		if k0 < 5:
			k0 = 8+7
			m4 = m4*5
			x = x*x
			paths.append(3)
		else:
			k0 = k0-1
			m4 = m4*7
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))