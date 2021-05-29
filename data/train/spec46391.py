import numpy as np 

def function(x):

	m4 = 8
	u5 = 9
	paths = []
	try:
		if m4 >= 8:
			u5 = 2/x
			paths.append(1)
		else:
			m4 = 2-m4
			m4 = 5*5
			m4 = 2+6
			paths.append(2)
		if x > 4:
			x = 1*x
			m4 = 6-m4
			paths.append(3)
		else:
			m4 = m4*0
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