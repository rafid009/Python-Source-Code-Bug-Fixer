import numpy as np 

def function(x):

	f5 = 3
	m8 = 9
	paths = []
	try:
		if m8 > 8:
			m8 = m8+x
			paths.append(1)
		else:
			f5 = x-m8
			paths.append(2)
		if f5 < 3:
			f5 = f5/m8
			x = 8*x
			m8 = f5*m8
			paths.append(3)
		else:
			m8 = f5+m8
			f5 = x+f5
			m8 = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m8 = x**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))