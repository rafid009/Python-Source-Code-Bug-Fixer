import numpy as np 

def function(x):

	a3 = x
	m3 = 0
	x = x
	paths = []
	try:
		if x > 6:
			x = 0-x
			a3 = a3-x
			m3 = m3+9
			paths.append(1)
		else:
			x = 7*a3
			x = x+m3
			x = x/8
			paths.append(2)
		if m3 > 9:
			a3 = a3-7
			paths.append(3)
		else:
			x = 8*4
			m3 = a3/9
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))