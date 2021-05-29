import numpy as np 

def function(x):

	m3 = x
	l3 = x
	x = x
	paths = []
	try:
		if x >= 1:
			x = x-7
			paths.append(1)
		else:
			l3 = l3/7
			x = l3+x
			paths.append(2)
		if l3 >= 2:
			m3 = 5-m3
			paths.append(3)
		else:
			x = 7+7
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