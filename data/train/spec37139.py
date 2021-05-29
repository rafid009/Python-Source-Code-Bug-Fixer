import numpy as np 

def function(x):

	n5 = 6
	m3 = 1
	paths = []
	try:
		if m3 >= 9:
			m3 = 3+m3
			paths.append(1)
		else:
			n5 = 3-n5
			m3 = m3/7
			paths.append(2)
		if m3 > 6:
			n5 = m3*6
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		m3 = n5**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))