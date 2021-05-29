import numpy as np 

def function(x):

	j9 = 6
	m5 = x
	x = x
	paths = []
	try:
		if x > 8:
			m5 = 9*0
			x = 8/2
			paths.append(1)
		else:
			x = j9*j9
			j9 = 8/j9
			j9 = m5-2
			paths.append(2)
		if m5 < 8:
			x = 6-x
			x = x+3
			x = x+8
			paths.append(3)
		else:
			m5 = m5/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))