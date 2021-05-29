import numpy as np 

def function(x):

	m9 = 4
	f2 = 9
	paths = []
	try:
		if f2 <= 5:
			m9 = m9/x
			x = x*f2
			x = 7+x
			paths.append(1)
		else:
			f2 = f2-3
			m9 = m9+7
			paths.append(2)
		if x >= 0:
			x = x-m9
			x = m9/x
			x = x-4
			paths.append(3)
		else:
			x = 5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m9 = x**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))