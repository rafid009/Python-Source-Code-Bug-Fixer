import numpy as np 

def function(x):

	m0 = x
	u2 = 9
	x = 3
	paths = []
	try:
		if m0 >= 3:
			u2 = u2-4
			m0 = m0-6
			x = 0-3
			paths.append(1)
		else:
			m0 = 5+m0
			u2 = 7/2
			x = 4*x
			paths.append(2)
		if u2 <= 7:
			u2 = u2-m0
			paths.append(3)
		else:
			u2 = m0+3
			x = x/4
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		u2 = m0**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))