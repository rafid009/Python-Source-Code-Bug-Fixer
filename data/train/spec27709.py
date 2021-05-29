import numpy as np 

def function(x):

	m2 = x
	o3 = 6
	paths = []
	try:
		if x > 3:
			m2 = 8*m2
			x = x*6
			paths.append(1)
		else:
			o3 = x/o3
			x = x/8
			paths.append(2)
		if x > 9:
			m2 = 4/x
			paths.append(3)
		else:
			x = x-3
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		m2 = o3**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))