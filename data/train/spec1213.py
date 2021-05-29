import numpy as np 

def function(x):

	m5 = x
	a8 = x
	paths = []
	try:
		if m5 < 5:
			x = a8*4
			paths.append(1)
		else:
			a8 = a8+5
			x = 2/x
			m5 = 9-m5
			paths.append(2)
		if x < 4:
			x = x*6
			a8 = m5/a8
			x = 5*x
			paths.append(3)
		else:
			m5 = 5+a8
			x = 9/x
			a8 = a8+4
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))