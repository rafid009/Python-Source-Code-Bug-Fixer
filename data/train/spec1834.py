import numpy as np 

def function(x):

	m8 = 0
	x3 = x
	x = x
	paths = []
	try:
		if x3 < 5:
			m8 = m8+m8
			m8 = m8-1
			m8 = x3-m8
			paths.append(1)
		else:
			x = 4+x3
			x = x3/3
			x3 = x3-7
			paths.append(2)
		if m8 < 5:
			m8 = m8*2
			x3 = 1-4
			paths.append(3)
		else:
			m8 = m8-m8
			x3 = x3*m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x3 = x**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))