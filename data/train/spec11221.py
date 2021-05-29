import numpy as np 

def function(x):

	m9 = x
	z9 = x
	x = 5
	paths = []
	try:
		if z9 < 4:
			m9 = 8+m9
			paths.append(1)
		else:
			m9 = m9-m9
			m9 = 9-x
			paths.append(2)
		if m9 < 2:
			m9 = z9-m9
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))