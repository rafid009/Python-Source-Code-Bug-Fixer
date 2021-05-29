import numpy as np 

def function(x):

	d5 = 2
	m5 = 7
	x = 3
	paths = []
	try:
		if d5 <= 3:
			x = x/x
			m5 = x/4
			x = 7-x
			paths.append(1)
		else:
			x = 5+m5
			paths.append(2)
		if x < 6:
			m5 = 5-m5
			x = 7+3
			x = 0*x
			paths.append(3)
		else:
			d5 = m5-4
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