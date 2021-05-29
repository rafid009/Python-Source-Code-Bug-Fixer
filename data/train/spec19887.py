import numpy as np 

def function(x):

	y8 = x
	m5 = x
	paths = []
	try:
		if y8 >= 7:
			m5 = m5+4
			x = x+9
			y8 = 6*y8
			paths.append(1)
		else:
			m5 = 5*y8
			x = m5+m5
			paths.append(2)
		if y8 < 6:
			y8 = 4+y8
			y8 = x/4
			x = 5*x
			paths.append(3)
		else:
			y8 = m5-m5
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