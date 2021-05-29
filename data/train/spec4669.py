import numpy as np 

def function(x):

	m9 = 3
	b0 = x
	paths = []
	try:
		if m9 >= 4:
			b0 = b0/m9
			b0 = 8*9
			b0 = 9-8
			paths.append(1)
		else:
			m9 = 6*3
			paths.append(2)
		if x >= 9:
			b0 = 4+m9
			m9 = m9/5
			paths.append(3)
		else:
			m9 = 4/m9
			m9 = b0-m9
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