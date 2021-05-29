import numpy as np 

def function(x):

	m0 = 4
	m1 = x
	paths = []
	try:
		if x >= 4:
			m0 = 8-9
			m1 = x/5
			paths.append(1)
		else:
			m0 = 6/8
			m0 = 5*m0
			x = 5/x
			paths.append(2)
		if m0 <= 6:
			m1 = m1+m1
			x = 5+x
			paths.append(3)
		else:
			m1 = 8+9
			x = x*1
			m1 = 1-m1
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m1 = m0**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))