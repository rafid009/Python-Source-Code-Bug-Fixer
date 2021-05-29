import numpy as np 

def function(x):

	m9 = x
	k4 = x
	paths = []
	try:
		if m9 > 3:
			k4 = 0-k4
			paths.append(1)
		else:
			m9 = m9-3
			m9 = m9*0
			m9 = 4*9
			paths.append(2)
		if k4 <= 1:
			k4 = 6/k4
			k4 = 5-k4
			m9 = x+3
			paths.append(3)
		else:
			m9 = m9-6
			x = 2-m9
			m9 = m9*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))