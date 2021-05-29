import numpy as np 

def function(x):

	m4 = 6
	f1 = 0
	paths = []
	try:
		if x <= 8:
			m4 = 6+m4
			f1 = x-3
			m4 = 7/5
			paths.append(1)
		else:
			f1 = f1-8
			x = 2-4
			m4 = f1+1
			paths.append(2)
		if m4 > 5:
			m4 = m4*1
			x = f1-4
			paths.append(3)
		else:
			x = m4/8
			m4 = m4-2
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