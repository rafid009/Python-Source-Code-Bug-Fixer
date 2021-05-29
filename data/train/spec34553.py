import numpy as np 

def function(x):

	y5 = 8
	m5 = x
	x = x
	paths = []
	try:
		if m5 < 2:
			y5 = 4/y5
			m5 = m5+m5
			x = 2/1
			paths.append(1)
		else:
			y5 = 4/x
			y5 = 3+6
			paths.append(2)
		if m5 <= 7:
			y5 = 9+m5
			m5 = 1+m5
			paths.append(3)
		else:
			x = 2-7
			m5 = 1*m5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		m5 = y5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))