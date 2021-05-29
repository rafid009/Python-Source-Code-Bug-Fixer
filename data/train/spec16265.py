import numpy as np 

def function(x):

	d8 = x
	m5 = 2
	paths = []
	try:
		if m5 < 7:
			m5 = d8*m5
			m5 = m5+2
			paths.append(1)
		else:
			d8 = 5+d8
			x = 8/x
			paths.append(2)
		if m5 <= 3:
			x = x-m5
			paths.append(3)
		else:
			x = x/d8
			d8 = 3-0
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))