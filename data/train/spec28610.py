import numpy as np 

def function(x):

	m9 = x
	f7 = 2
	paths = []
	try:
		if f7 <= 0:
			f7 = f7/f7
			paths.append(1)
		else:
			x = 6*x
			f7 = 8-1
			paths.append(2)
		if m9 <= 6:
			x = 1/x
			paths.append(3)
		else:
			m9 = m9*m9
			f7 = 8/f7
			x = 6/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))