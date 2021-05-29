import numpy as np 

def function(x):

	m7 = x
	f7 = x
	paths = []
	try:
		if f7 <= 9:
			m7 = 3+m7
			paths.append(1)
		else:
			m7 = x-x
			f7 = f7*f7
			paths.append(2)
		if f7 <= 2:
			x = x+3
			paths.append(3)
		else:
			f7 = 7-0
			x = 3/x
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))