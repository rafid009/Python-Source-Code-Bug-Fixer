import numpy as np 

def function(x):

	f6 = 7
	m4 = x
	paths = []
	try:
		if x < 9:
			f6 = f6-1
			m4 = f6+m4
			f6 = 7+x
			paths.append(1)
		else:
			f6 = 0+f6
			paths.append(2)
		if m4 >= 1:
			m4 = m4/f6
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))