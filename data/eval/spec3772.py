import numpy as np 

def function(x):

	q6 = x
	m3 = x
	x = x
	paths = []
	try:
		if m3 < 5:
			x = x*m3
			m3 = 0/m3
			x = 0-2
			paths.append(1)
		else:
			q6 = 0+q6
			m3 = 5-m3
			paths.append(2)
		if m3 > 6:
			x = q6/x
			paths.append(3)
		else:
			m3 = x*m3
			q6 = x+4
			x = x/3
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