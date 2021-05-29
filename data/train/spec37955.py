import numpy as np 

def function(x):

	m3 = x
	e3 = x
	paths = []
	try:
		if x <= 6:
			e3 = e3*e3
			paths.append(1)
		else:
			x = x-9
			m3 = m3-7
			m3 = m3-e3
			paths.append(2)
		if x < 0:
			e3 = x*5
			m3 = x+m3
			e3 = e3-1
			paths.append(3)
		else:
			m3 = m3+1
			m3 = 6-m3
			e3 = 1*x
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