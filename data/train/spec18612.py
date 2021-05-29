import numpy as np 

def function(x):

	m0 = x
	i4 = 6
	paths = []
	try:
		if m0 > 9:
			x = 4*1
			x = 4*x
			paths.append(1)
		else:
			i4 = i4-i4
			m0 = m0-i4
			paths.append(2)
		if x < 2:
			i4 = i4+i4
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))