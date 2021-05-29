import numpy as np 

def function(x):

	x4 = x
	m5 = x
	x = x
	paths = []
	try:
		if x4 >= 3:
			x4 = 0*x
			m5 = x4-6
			paths.append(1)
		else:
			x4 = x*5
			paths.append(2)
		if x4 <= 7:
			m5 = m5/9
			paths.append(3)
		else:
			x4 = m5-6
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		m5 = x4**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))