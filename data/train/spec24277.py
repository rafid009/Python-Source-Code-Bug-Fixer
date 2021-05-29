import numpy as np 

def function(x):

	y1 = 0
	m5 = x
	paths = []
	try:
		if m5 < 8:
			x = m5*m5
			paths.append(1)
		else:
			x = 8*m5
			y1 = 3*m5
			paths.append(2)
		if m5 < 4:
			x = 1/x
			paths.append(3)
		else:
			m5 = 6/9
			y1 = y1-y1
			x = 5/3
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