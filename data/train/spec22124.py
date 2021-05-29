import numpy as np 

def function(x):

	m3 = x
	m2 = x
	x = x
	paths = []
	try:
		if x >= 4:
			m2 = 6+m2
			paths.append(1)
		else:
			m3 = m3-8
			paths.append(2)
		if x <= 2:
			m3 = 9-m3
			x = x/m3
			x = x+0
			paths.append(3)
		else:
			x = x+7
			m3 = m3/6
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))