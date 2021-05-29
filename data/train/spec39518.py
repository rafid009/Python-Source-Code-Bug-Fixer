import numpy as np 

def function(x):

	e8 = x
	m8 = x
	paths = []
	try:
		if e8 > 0:
			m8 = m8+0
			paths.append(1)
		else:
			x = x/4
			m8 = 3-m8
			e8 = e8/5
			paths.append(2)
		if m8 <= 7:
			m8 = 9+e8
			e8 = x*2
			paths.append(3)
		else:
			e8 = 5+x
			x = x-e8
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