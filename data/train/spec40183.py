import numpy as np 

def function(x):

	f8 = 6
	m3 = x
	x = 6
	paths = []
	try:
		if m3 <= 1:
			f8 = 5/8
			f8 = f8/x
			paths.append(1)
		else:
			x = x/6
			x = x-x
			x = x/f8
			paths.append(2)
		if x <= 9:
			x = f8/m3
			paths.append(3)
		else:
			x = x-3
			x = 7*m3
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