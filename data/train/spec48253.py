import numpy as np 

def function(x):

	f4 = 5
	m5 = x
	paths = []
	try:
		if x > 0:
			m5 = m5/9
			x = 3+2
			paths.append(1)
		else:
			x = 9*8
			paths.append(2)
		if x > 7:
			x = x*m5
			paths.append(3)
		else:
			m5 = 8*m5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))