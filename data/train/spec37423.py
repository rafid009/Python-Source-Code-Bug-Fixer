import numpy as np 

def function(x):

	u7 = 5
	m0 = 5
	paths = []
	try:
		if m0 >= 0:
			u7 = u7-7
			paths.append(1)
		else:
			u7 = 2+7
			u7 = 4+u7
			paths.append(2)
		if x > 1:
			m0 = m0-5
			x = m0*1
			x = x+4
			paths.append(3)
		else:
			m0 = m0/m0
			m0 = 5*x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		u7 = m0**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))