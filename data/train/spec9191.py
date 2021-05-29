import numpy as np 

def function(x):

	m8 = 5
	e6 = x
	paths = []
	try:
		if x < 7:
			x = x-6
			e6 = e6*e6
			e6 = 5+e6
			paths.append(1)
		else:
			x = 9+x
			x = 2+x
			paths.append(2)
		if e6 <= 8:
			m8 = m8*8
			m8 = 2-x
			x = x+8
			paths.append(3)
		else:
			e6 = 4*e6
			x = x/x
			m8 = m8/4
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		e6 = m8**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))