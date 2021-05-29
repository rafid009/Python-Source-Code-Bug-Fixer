import numpy as np 

def function(x):

	m5 = x
	t4 = x
	paths = []
	try:
		if x > 1:
			m5 = m5*5
			x = x*6
			t4 = m5*t4
			paths.append(1)
		else:
			m5 = 2*m5
			paths.append(2)
		if t4 > 2:
			x = 1+6
			m5 = t4-7
			paths.append(3)
		else:
			m5 = 8/t4
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		x = t4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))