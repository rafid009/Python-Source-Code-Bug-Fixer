import numpy as np 

def function(x):

	m5 = 7
	a7 = x
	paths = []
	try:
		if x <= 7:
			m5 = 4-4
			a7 = 1/a7
			x = 4-x
			paths.append(1)
		else:
			x = 7-4
			paths.append(2)
		if a7 <= 9:
			m5 = m5+5
			x = m5+9
			paths.append(3)
		else:
			m5 = 7+m5
			m5 = x-9
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