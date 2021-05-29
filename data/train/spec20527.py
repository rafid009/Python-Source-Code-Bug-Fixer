import numpy as np 

def function(x):

	m5 = x
	r5 = 3
	paths = []
	try:
		if x >= 6:
			m5 = m5*4
			r5 = 7-r5
			paths.append(1)
		else:
			x = x+m5
			r5 = 0-r5
			paths.append(2)
		if r5 < 5:
			r5 = x-4
			r5 = 2/9
			paths.append(3)
		else:
			m5 = 6-m5
			r5 = r5/r5
			m5 = m5/5
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