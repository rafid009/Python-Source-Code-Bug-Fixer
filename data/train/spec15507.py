import numpy as np 

def function(x):

	y4 = x
	m9 = 8
	paths = []
	try:
		if m9 >= 6:
			y4 = 1+0
			m9 = m9*x
			paths.append(1)
		else:
			y4 = 8*y4
			paths.append(2)
		if m9 > 8:
			y4 = 6+m9
			m9 = m9*0
			m9 = 1*m9
			paths.append(3)
		else:
			y4 = 8*x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))