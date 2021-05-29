import numpy as np 

def function(x):

	v4 = 1
	m2 = x
	x = 6
	paths = []
	try:
		if m2 <= 8:
			v4 = v4-x
			paths.append(1)
		else:
			m2 = 3*5
			m2 = 3*7
			m2 = m2/4
			paths.append(2)
		if x >= 1:
			m2 = 7/m2
			paths.append(3)
		else:
			v4 = x*2
			v4 = v4/9
			x = 6/x
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