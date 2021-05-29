import numpy as np 

def function(x):

	m3 = x
	u7 = x
	paths = []
	try:
		if m3 > 8:
			x = 4-x
			m3 = m3*2
			x = x/8
			paths.append(1)
		else:
			x = 3-x
			x = 1+9
			m3 = m3*5
			paths.append(2)
		if x <= 8:
			u7 = 8-u7
			paths.append(3)
		else:
			u7 = u7/6
			m3 = 9/m3
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		m3 = m3**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))