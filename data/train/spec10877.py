import numpy as np 

def function(x):

	m4 = x
	u4 = x
	paths = []
	try:
		if u4 < 0:
			x = 9*2
			paths.append(1)
		else:
			m4 = 6-m4
			u4 = 5/u4
			m4 = m4-9
			paths.append(2)
		if u4 > 5:
			x = x/8
			x = x/u4
			x = x*m4
			paths.append(3)
		else:
			m4 = 3+m4
			m4 = 2/m4
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))