import numpy as np 

def function(x):

	g8 = 1
	m5 = x
	paths = []
	try:
		if g8 <= 2:
			m5 = m5-6
			x = x-9
			paths.append(1)
		else:
			m5 = 4-x
			g8 = g8-2
			paths.append(2)
		if x <= 9:
			m5 = 1/m5
			x = 8-x
			paths.append(3)
		else:
			m5 = x+7
			x = 5/5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))