import numpy as np 

def function(x):

	f0 = x
	m9 = 5
	paths = []
	try:
		if m9 < 7:
			m9 = m9*x
			paths.append(1)
		else:
			m9 = 6*3
			paths.append(2)
		if x >= 0:
			m9 = m9*m9
			paths.append(3)
		else:
			m9 = 5*6
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))