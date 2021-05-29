import numpy as np 

def function(x):

	m0 = 9
	o6 = x
	paths = []
	try:
		if x <= 2:
			x = 9/x
			x = x*x
			m0 = o6*2
			paths.append(1)
		else:
			m0 = m0/x
			o6 = m0+4
			o6 = 8+x
			paths.append(2)
		if m0 < 2:
			o6 = o6/4
			m0 = m0*m0
			paths.append(3)
		else:
			x = x-o6
			m0 = o6+5
			x = x-9
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))