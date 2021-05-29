import numpy as np 

def function(x):

	m9 = 0
	x8 = x
	paths = []
	try:
		if m9 > 4:
			m9 = 8*m9
			x8 = x8*2
			x8 = 2/x
			paths.append(1)
		else:
			x8 = m9-x
			paths.append(2)
		if x >= 3:
			x = x*8
			m9 = 6+m9
			paths.append(3)
		else:
			x8 = x8/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))