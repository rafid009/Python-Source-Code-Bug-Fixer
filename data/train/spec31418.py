import numpy as np 

def function(x):

	m7 = 3
	f7 = x
	x = 1
	paths = []
	try:
		if f7 >= 2:
			x = 4/x
			paths.append(1)
		else:
			x = f7-5
			paths.append(2)
		if f7 > 9:
			f7 = f7*8
			paths.append(3)
		else:
			f7 = 5+f7
			m7 = x+4
			x = x/m7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))