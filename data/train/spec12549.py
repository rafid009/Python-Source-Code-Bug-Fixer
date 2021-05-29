import numpy as np 

def function(x):

	o0 = x
	m0 = 2
	x = x
	paths = []
	try:
		if o0 < 6:
			o0 = 5+0
			m0 = m0*5
			m0 = m0+0
			paths.append(1)
		else:
			m0 = 0*1
			m0 = m0+8
			paths.append(2)
		if x < 2:
			x = x+2
			m0 = x*9
			x = m0/m0
			paths.append(3)
		else:
			x = o0-x
			m0 = 4-m0
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