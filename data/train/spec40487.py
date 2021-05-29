import numpy as np 

def function(x):

	f6 = x
	m8 = x
	paths = []
	try:
		if x >= 3:
			f6 = f6*4
			paths.append(1)
		else:
			m8 = m8*f6
			m8 = m8-m8
			f6 = 4*f6
			paths.append(2)
		if f6 > 0:
			f6 = m8*2
			paths.append(3)
		else:
			f6 = f6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))