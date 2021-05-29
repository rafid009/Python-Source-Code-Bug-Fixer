import numpy as np 

def function(x):

	m4 = 6
	f0 = 6
	paths = []
	try:
		if m4 <= 6:
			x = x+2
			paths.append(1)
		else:
			f0 = x/f0
			f0 = f0-2
			f0 = m4+f0
			paths.append(2)
		if x <= 1:
			f0 = 9/f0
			m4 = m4+7
			paths.append(3)
		else:
			f0 = f0+5
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