import numpy as np 

def function(x):

	o7 = x
	m5 = 0
	x = 6
	paths = []
	try:
		if x >= 9:
			x = x-9
			x = x-5
			paths.append(1)
		else:
			x = x-m5
			o7 = 2-o7
			paths.append(2)
		if x < 1:
			o7 = 9/x
			paths.append(3)
		else:
			m5 = x/o7
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		m5 = m5**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))