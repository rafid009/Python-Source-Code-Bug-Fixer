import numpy as np 

def function(x):

	m3 = x
	o3 = 8
	paths = []
	try:
		if m3 > 1:
			m3 = o3+o3
			m3 = 2/6
			paths.append(1)
		else:
			m3 = m3/7
			x = x/x
			paths.append(2)
		if x > 6:
			o3 = x/o3
			paths.append(3)
		else:
			o3 = 2*o3
			m3 = m3-9
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))