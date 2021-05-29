import numpy as np 

def function(x):

	m3 = x
	f4 = 7
	paths = []
	try:
		if f4 >= 8:
			f4 = 9*f4
			paths.append(1)
		else:
			m3 = 1/m3
			x = x+x
			f4 = f4*7
			paths.append(2)
		if x >= 8:
			f4 = 5-f4
			x = x-0
			paths.append(3)
		else:
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))