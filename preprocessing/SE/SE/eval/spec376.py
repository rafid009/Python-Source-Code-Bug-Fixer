import numpy as np 

def function(x):

	k7 = x
	m4 = 5
	paths = []
	try:
		if m4 >= 3:
			x = x*3
			x = 0-5
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x >= 3:
			x = x/k7
			k7 = k7-0
			paths.append(3)
		else:
			m4 = 8*m4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))