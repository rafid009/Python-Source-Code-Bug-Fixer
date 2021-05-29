import numpy as np 

def function(x):

	m5 = 8
	u4 = 9
	paths = []
	try:
		if x >= 6:
			m5 = m5/9
			x = x/u4
			x = x-6
			paths.append(1)
		else:
			u4 = u4+9
			paths.append(2)
		if m5 < 2:
			u4 = m5*u4
			m5 = 7/2
			m5 = m5*m5
			paths.append(3)
		else:
			m5 = 8/m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))