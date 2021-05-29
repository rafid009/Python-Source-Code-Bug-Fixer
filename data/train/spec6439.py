import numpy as np 

def function(x):

	m3 = 5
	f2 = 5
	paths = []
	try:
		if f2 > 3:
			f2 = f2*f2
			m3 = m3/f2
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if m3 <= 1:
			f2 = f2-2
			paths.append(3)
		else:
			x = 5+3
			m3 = m3*7
			f2 = f2/m3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))