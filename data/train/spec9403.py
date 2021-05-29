import numpy as np 

def function(x):

	m3 = x
	i0 = x
	paths = []
	try:
		if i0 >= 2:
			m3 = m3/5
			x = 5-m3
			i0 = 3-4
			paths.append(1)
		else:
			i0 = i0*0
			paths.append(2)
		if m3 > 6:
			i0 = m3+9
			paths.append(3)
		else:
			m3 = 2/m3
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