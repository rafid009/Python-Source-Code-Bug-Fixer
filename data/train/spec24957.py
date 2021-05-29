import numpy as np 

def function(x):

	m4 = 9
	f9 = x
	paths = []
	try:
		if f9 > 3:
			f9 = x*f9
			f9 = 4+f9
			x = x-m4
			paths.append(1)
		else:
			x = 2-x
			f9 = 7+f9
			f9 = m4-9
			paths.append(2)
		if f9 <= 8:
			x = 7*x
			paths.append(3)
		else:
			f9 = f9*2
			m4 = m4/4
			x = m4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))