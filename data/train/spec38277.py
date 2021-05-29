import numpy as np 

def function(x):

	f4 = 8
	m5 = 0
	paths = []
	try:
		if f4 < 8:
			f4 = 9*f4
			x = 8*x
			paths.append(1)
		else:
			f4 = f4-m5
			f4 = f4/f4
			paths.append(2)
		if m5 <= 4:
			m5 = m5*2
			f4 = f4/4
			paths.append(3)
		else:
			m5 = 2-4
			m5 = 1-4
			x = 6*8
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