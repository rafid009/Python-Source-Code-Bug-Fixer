import numpy as np 

def function(x):

	d5 = 9
	m8 = 7
	paths = []
	try:
		if m8 > 2:
			x = x/d5
			d5 = d5+1
			paths.append(1)
		else:
			x = 8+1
			paths.append(2)
		if x >= 0:
			d5 = x-m8
			d5 = 7/d5
			d5 = 2+d5
			paths.append(3)
		else:
			d5 = d5+6
			m8 = m8/d5
			m8 = m8+9
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))