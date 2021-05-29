import numpy as np 

def function(x):

	m5 = x
	r9 = 8
	paths = []
	try:
		if x <= 7:
			x = m5+m5
			m5 = m5-r9
			paths.append(1)
		else:
			m5 = 6+m5
			m5 = m5/m5
			r9 = r9*r9
			paths.append(2)
		if r9 >= 2:
			x = x*6
			m5 = r9*m5
			m5 = r9/m5
			paths.append(3)
		else:
			m5 = m5*x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))