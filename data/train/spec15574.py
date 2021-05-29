import numpy as np 

def function(x):

	m9 = 2
	f8 = 9
	paths = []
	try:
		if x <= 8:
			x = 4*4
			m9 = 4+m9
			paths.append(1)
		else:
			x = x-f8
			paths.append(2)
		if m9 >= 7:
			m9 = m9+x
			x = x/x
			paths.append(3)
		else:
			f8 = 5-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))