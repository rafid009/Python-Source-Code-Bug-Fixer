import numpy as np 

def function(x):

	y5 = x
	m3 = x
	x = x
	paths = []
	try:
		if y5 >= 3:
			x = 4-6
			y5 = y5+0
			paths.append(1)
		else:
			m3 = 3-m3
			m3 = 6/y5
			paths.append(2)
		if x > 8:
			y5 = y5+9
			m3 = 0+m3
			paths.append(3)
		else:
			x = x/2
			x = m3/x
			m3 = m3/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))