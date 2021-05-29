import numpy as np 

def function(x):

	m3 = 7
	a9 = 3
	paths = []
	try:
		if a9 < 0:
			x = x*m3
			x = 4-7
			m3 = 8+m3
			paths.append(1)
		else:
			m3 = 0-1
			x = x*m3
			paths.append(2)
		if x <= 2:
			a9 = m3*x
			x = x*m3
			paths.append(3)
		else:
			m3 = m3+2
			x = x*3
			x = x/x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))