import numpy as np 

def function(x):

	m4 = 4
	k4 = 6
	paths = []
	try:
		if k4 <= 5:
			x = x-1
			m4 = 2*m4
			x = m4/x
			paths.append(1)
		else:
			k4 = 2*9
			paths.append(2)
		if k4 > 3:
			m4 = x/m4
			paths.append(3)
		else:
			x = 8+x
			x = x-8
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		k4 = m4**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))