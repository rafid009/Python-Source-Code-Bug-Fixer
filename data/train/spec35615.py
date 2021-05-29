import numpy as np 

def function(x):

	n4 = 9
	m3 = x
	x = x
	paths = []
	try:
		if n4 < 9:
			x = 4*x
			paths.append(1)
		else:
			n4 = x-0
			x = n4/8
			paths.append(2)
		if x > 9:
			x = m3-x
			n4 = 4*0
			paths.append(3)
		else:
			n4 = n4*5
			m3 = m3*3
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