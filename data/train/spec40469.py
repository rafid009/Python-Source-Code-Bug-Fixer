import numpy as np 

def function(x):

	f4 = x
	m7 = 6
	paths = []
	try:
		if f4 > 5:
			f4 = 6+7
			m7 = m7*x
			f4 = 3-f4
			paths.append(1)
		else:
			f4 = x-f4
			paths.append(2)
		if m7 <= 2:
			x = 8*x
			paths.append(3)
		else:
			x = f4+5
			f4 = 7/6
			m7 = 0*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))