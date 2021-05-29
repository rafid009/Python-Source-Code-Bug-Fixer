import numpy as np 

def function(x):

	m3 = x
	v0 = x
	paths = []
	try:
		if v0 < 5:
			x = 3+1
			x = 2+x
			x = v0/2
			paths.append(1)
		else:
			x = x-1
			x = 9+x
			paths.append(2)
		if m3 > 6:
			v0 = v0-3
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))