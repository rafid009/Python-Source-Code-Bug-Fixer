import numpy as np 

def function(x):

	x5 = x
	m5 = 2
	paths = []
	try:
		if x > 2:
			m5 = 2*5
			x = x5+x5
			m5 = 1-8
			paths.append(1)
		else:
			m5 = m5-4
			x = 8+3
			x = x-5
			paths.append(2)
		if x5 <= 6:
			x = m5*6
			x = x*m5
			paths.append(3)
		else:
			x = m5-x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))