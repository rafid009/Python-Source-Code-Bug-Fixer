import numpy as np 

def function(x):

	a4 = x
	m3 = 3
	paths = []
	try:
		if x < 9:
			m3 = m3-0
			paths.append(1)
		else:
			a4 = a4/x
			m3 = 8/m3
			paths.append(2)
		if m3 < 9:
			a4 = 0-a4
			m3 = 5-8
			m3 = m3*x
			paths.append(3)
		else:
			x = x/5
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		a4 = m3**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))