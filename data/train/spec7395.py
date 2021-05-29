import numpy as np 

def function(x):

	y6 = x
	m7 = 3
	paths = []
	try:
		if m7 <= 0:
			x = x-0
			paths.append(1)
		else:
			y6 = x*y6
			m7 = m7*2
			m7 = m7-y6
			paths.append(2)
		if y6 > 9:
			m7 = m7+m7
			paths.append(3)
		else:
			y6 = m7-y6
			y6 = y6-4
			y6 = 3/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))