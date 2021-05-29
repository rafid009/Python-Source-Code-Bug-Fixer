import numpy as np 

def function(x):

	k7 = 1
	m4 = x
	paths = []
	try:
		if k7 < 2:
			k7 = 5/k7
			paths.append(1)
		else:
			x = 6+m4
			m4 = 3*m4
			paths.append(2)
		if x > 7:
			m4 = k7*7
			x = x*1
			paths.append(3)
		else:
			m4 = 4*m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))