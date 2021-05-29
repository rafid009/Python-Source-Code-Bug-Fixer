import numpy as np 

def function(x):

	m8 = x
	x4 = x
	x = x
	paths = []
	try:
		if x4 <= 3:
			x = x/3
			m8 = 0+7
			paths.append(1)
		else:
			x = 0-x
			x4 = 5-m8
			m8 = x*m8
			paths.append(2)
		if m8 > 4:
			m8 = x+m8
			x = x-1
			x4 = m8*4
			paths.append(3)
		else:
			x = m8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))