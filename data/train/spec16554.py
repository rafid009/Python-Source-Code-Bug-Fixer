import numpy as np 

def function(x):

	u2 = x
	m8 = x
	paths = []
	try:
		if u2 < 1:
			u2 = 3*u2
			x = 5-7
			u2 = 3/9
			paths.append(1)
		else:
			u2 = u2*7
			paths.append(2)
		if u2 <= 7:
			x = 0/u2
			m8 = m8+x
			paths.append(3)
		else:
			m8 = 0+u2
			m8 = m8-x
			u2 = u2+2
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		m8 = m8**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))