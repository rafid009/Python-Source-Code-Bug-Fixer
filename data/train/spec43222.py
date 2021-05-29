import numpy as np 

def function(x):

	y8 = x
	m2 = x
	paths = []
	try:
		if x <= 9:
			m2 = m2-y8
			x = 1+x
			paths.append(1)
		else:
			x = m2-x
			m2 = 0/m2
			m2 = m2+4
			paths.append(2)
		if m2 <= 7:
			x = x*y8
			paths.append(3)
		else:
			y8 = 5+y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		m2 = y8**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))