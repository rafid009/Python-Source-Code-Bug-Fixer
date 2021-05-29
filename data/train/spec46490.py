import numpy as np 

def function(x):

	m3 = 0
	o3 = 3
	paths = []
	try:
		if m3 < 4:
			m3 = 6/5
			m3 = 0+x
			m3 = 9-m3
			paths.append(1)
		else:
			m3 = m3-5
			paths.append(2)
		if m3 < 6:
			o3 = o3/1
			x = 7+x
			paths.append(3)
		else:
			m3 = 4-m3
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