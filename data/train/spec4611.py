import numpy as np 

def function(x):

	m3 = x
	y8 = 9
	paths = []
	try:
		if x <= 4:
			x = 5+x
			m3 = y8*m3
			x = x/2
			paths.append(1)
		else:
			m3 = m3+4
			paths.append(2)
		if m3 >= 8:
			y8 = 1/y8
			paths.append(3)
		else:
			x = x*9
			x = 3-x
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