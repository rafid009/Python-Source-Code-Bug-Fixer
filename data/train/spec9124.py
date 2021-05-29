import numpy as np 

def function(x):

	m2 = x
	f3 = x
	paths = []
	try:
		if m2 >= 2:
			x = x*7
			x = 2-7
			paths.append(1)
		else:
			x = f3/2
			m2 = m2+3
			x = m2*7
			paths.append(2)
		if f3 > 9:
			f3 = 8-x
			f3 = 9+f3
			paths.append(3)
		else:
			m2 = m2+2
			m2 = m2+2
			m2 = m2+4
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))