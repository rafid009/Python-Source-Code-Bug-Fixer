import numpy as np 

def function(x):

	o2 = 8
	m7 = x
	paths = []
	try:
		if x >= 7:
			m7 = m7/4
			m7 = 6-x
			paths.append(1)
		else:
			o2 = o2-7
			paths.append(2)
		if x <= 3:
			x = x/m7
			x = x-8
			m7 = 8-9
			paths.append(3)
		else:
			o2 = o2*m7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))