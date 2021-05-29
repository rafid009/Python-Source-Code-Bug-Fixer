import numpy as np 

def function(x):

	o8 = 8
	m8 = 8
	paths = []
	try:
		if m8 <= 5:
			x = x/3
			m8 = 8-2
			paths.append(1)
		else:
			o8 = o8-4
			paths.append(2)
		if m8 <= 2:
			m8 = o8/7
			paths.append(3)
		else:
			m8 = m8/9
			m8 = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))