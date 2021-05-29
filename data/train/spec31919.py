import numpy as np 

def function(x):

	m5 = 4
	v7 = 9
	paths = []
	try:
		if v7 < 7:
			m5 = m5-x
			paths.append(1)
		else:
			x = x/7
			v7 = 9+v7
			v7 = 6-v7
			paths.append(2)
		if m5 < 3:
			m5 = m5*7
			paths.append(3)
		else:
			m5 = 7*6
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		m5 = v7**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))