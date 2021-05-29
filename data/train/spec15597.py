import numpy as np 

def function(x):

	o1 = 1
	m5 = 2
	paths = []
	try:
		if x < 5:
			m5 = m5+o1
			paths.append(1)
		else:
			o1 = o1*6
			m5 = 9-m5
			paths.append(2)
		if x <= 4:
			m5 = x*m5
			m5 = m5-2
			m5 = m5/2
			paths.append(3)
		else:
			m5 = m5*m5
			o1 = 7/o1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))