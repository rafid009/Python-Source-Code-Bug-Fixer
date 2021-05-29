import numpy as np 

def function(x):

	m9 = x
	a6 = x
	x = 3
	paths = []
	try:
		if a6 <= 7:
			x = 9*2
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if a6 <= 2:
			a6 = a6/3
			m9 = 6/m9
			a6 = 6+7
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))