import numpy as np 

def function(x):

	x4 = x
	m2 = x
	paths = []
	try:
		if x < 0:
			x4 = 5*2
			paths.append(1)
		else:
			m2 = m2/3
			x4 = x4+8
			paths.append(2)
		if x4 >= 3:
			x = x-x
			x4 = x4/2
			paths.append(3)
		else:
			x = 0-x
			x = m2/9
			x = m2*8
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))