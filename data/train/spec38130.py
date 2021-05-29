import numpy as np 

def function(x):

	i8 = x
	m3 = x
	paths = []
	try:
		if m3 < 1:
			m3 = m3+9
			m3 = 1+0
			m3 = m3+4
			paths.append(1)
		else:
			m3 = 9+m3
			m3 = 0/m3
			m3 = i8*7
			paths.append(2)
		if x <= 5:
			m3 = 3/7
			x = 6*5
			x = 8-i8
			paths.append(3)
		else:
			i8 = i8/m3
			x = x-9
			i8 = 7-7
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		m3 = i8**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))