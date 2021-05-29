import numpy as np 

def function(x):

	m3 = 5
	i7 = x
	paths = []
	try:
		if m3 < 0:
			i7 = x/2
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if i7 >= 7:
			x = 8/3
			x = 6*x
			i7 = i7/i7
			paths.append(3)
		else:
			m3 = 4/i7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))