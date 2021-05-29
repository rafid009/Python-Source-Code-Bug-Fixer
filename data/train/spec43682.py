import numpy as np 

def function(x):

	m2 = x
	k7 = 8
	x = x
	paths = []
	try:
		if k7 <= 3:
			m2 = x+3
			paths.append(1)
		else:
			k7 = k7-7
			k7 = k7/1
			k7 = x*x
			paths.append(2)
		if x >= 9:
			m2 = m2/4
			paths.append(3)
		else:
			x = 3*7
			m2 = m2*6
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