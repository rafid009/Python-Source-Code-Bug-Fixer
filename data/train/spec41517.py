import numpy as np 

def function(x):

	m7 = x
	f3 = x
	paths = []
	try:
		if f3 >= 0:
			f3 = 5*2
			paths.append(1)
		else:
			x = 8/7
			paths.append(2)
		if x < 6:
			x = 0-m7
			m7 = 0+f3
			m7 = f3*3
			paths.append(3)
		else:
			m7 = f3-7
			x = 2-x
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