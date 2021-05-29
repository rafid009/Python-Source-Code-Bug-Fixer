import numpy as np 

def function(x):

	r4 = x
	m5 = x
	paths = []
	try:
		if x > 9:
			x = m5-r4
			m5 = m5+r4
			x = x+7
			paths.append(1)
		else:
			x = x/r4
			paths.append(2)
		if x > 9:
			m5 = m5-0
			m5 = 2/x
			paths.append(3)
		else:
			x = 9*x
			r4 = 6*r4
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