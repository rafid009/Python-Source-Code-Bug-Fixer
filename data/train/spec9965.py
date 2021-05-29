import numpy as np 

def function(x):

	j6 = 2
	m3 = x
	paths = []
	try:
		if j6 <= 0:
			m3 = 3/4
			x = 7-j6
			paths.append(1)
		else:
			j6 = 2+4
			m3 = 9*x
			paths.append(2)
		if j6 >= 4:
			j6 = 6-m3
			x = j6-5
			paths.append(3)
		else:
			m3 = m3+2
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