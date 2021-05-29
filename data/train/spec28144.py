import numpy as np 

def function(x):

	m5 = x
	d2 = 1
	paths = []
	try:
		if d2 < 8:
			x = x/x
			x = x/2
			d2 = 3+m5
			paths.append(1)
		else:
			x = 9*4
			d2 = d2/4
			paths.append(2)
		if m5 > 2:
			m5 = d2*m5
			paths.append(3)
		else:
			x = 9/x
			x = x/3
			x = x+9
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		m5 = d2**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))