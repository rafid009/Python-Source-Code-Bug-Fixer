import numpy as np 

def function(x):

	y6 = 7
	m7 = x
	paths = []
	try:
		if x <= 4:
			m7 = x+m7
			x = x/2
			paths.append(1)
		else:
			x = 5-m7
			paths.append(2)
		if y6 > 0:
			m7 = m7/4
			paths.append(3)
		else:
			y6 = m7+y6
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