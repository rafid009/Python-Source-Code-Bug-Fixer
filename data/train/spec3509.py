import numpy as np 

def function(x):

	m2 = 0
	i3 = x
	paths = []
	try:
		if x < 9:
			i3 = m2+4
			paths.append(1)
		else:
			m2 = x+m2
			i3 = i3-4
			paths.append(2)
		if x <= 2:
			m2 = m2+3
			i3 = 8+x
			paths.append(3)
		else:
			x = x-i3
			i3 = 4*i3
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