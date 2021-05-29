import numpy as np 

def function(x):

	m0 = x
	u7 = 9
	paths = []
	try:
		if u7 >= 5:
			u7 = 4+u7
			paths.append(1)
		else:
			x = x+m0
			m0 = m0+x
			m0 = 8-m0
			paths.append(2)
		if m0 <= 9:
			x = 4*4
			x = m0-5
			x = x-4
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))