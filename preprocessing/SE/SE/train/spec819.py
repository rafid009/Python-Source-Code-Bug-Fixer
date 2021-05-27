import numpy as np 

def function(x):

	m2 = x
	a0 = x
	paths = []
	try:
		if a0 <= 8:
			x = x+9
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if m2 > 0:
			m2 = 0*m2
			paths.append(3)
		else:
			x = 9-x
			a0 = a0+6
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		m2 = a0**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))