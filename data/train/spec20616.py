import numpy as np 

def function(x):

	m8 = 5
	f4 = x
	paths = []
	try:
		if f4 > 9:
			f4 = 2/2
			x = x-0
			f4 = f4/x
			paths.append(1)
		else:
			f4 = f4*6
			paths.append(2)
		if f4 < 5:
			f4 = f4*7
			paths.append(3)
		else:
			f4 = f4-5
			m8 = x*m8
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		m8 = f4**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))