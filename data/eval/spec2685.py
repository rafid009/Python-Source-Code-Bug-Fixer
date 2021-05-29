import numpy as np 

def function(x):

	y6 = x
	m7 = 2
	paths = []
	try:
		if m7 < 5:
			y6 = y6+0
			y6 = 8+0
			paths.append(1)
		else:
			y6 = y6-4
			y6 = 2-y6
			paths.append(2)
		if y6 > 3:
			x = 9/x
			m7 = 1+4
			m7 = m7+7
			paths.append(3)
		else:
			y6 = 2+7
			m7 = m7+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))