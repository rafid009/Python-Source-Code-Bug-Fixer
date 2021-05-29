import numpy as np 

def function(x):

	m8 = x
	i5 = x
	paths = []
	try:
		if m8 > 4:
			m8 = 1-m8
			m8 = i5*m8
			x = i5+1
			paths.append(1)
		else:
			m8 = 0-0
			paths.append(2)
		if i5 >= 4:
			i5 = 9/7
			x = x-9
			i5 = 8+5
			paths.append(3)
		else:
			i5 = i5-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))