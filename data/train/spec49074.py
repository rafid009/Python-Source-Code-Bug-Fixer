import numpy as np 

def function(x):

	x5 = 4
	m9 = x
	paths = []
	try:
		if m9 <= 1:
			m9 = 5-m9
			paths.append(1)
		else:
			x5 = x/6
			x = x*x
			x = x+8
			paths.append(2)
		if x5 <= 0:
			x5 = 9+5
			x = x/2
			paths.append(3)
		else:
			m9 = m9-7
			m9 = 5/m9
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