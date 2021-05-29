import numpy as np 

def function(x):

	g5 = 6
	m4 = x
	paths = []
	try:
		if m4 <= 7:
			g5 = m4/g5
			x = 9-0
			paths.append(1)
		else:
			m4 = m4*9
			x = 7/x
			paths.append(2)
		if m4 > 9:
			m4 = 5+3
			g5 = 1-8
			g5 = 8/g5
			paths.append(3)
		else:
			g5 = m4+1
			g5 = 1/2
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))