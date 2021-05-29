import numpy as np 

def function(x):

	m3 = 3
	o0 = x
	paths = []
	try:
		if x < 7:
			x = x+3
			o0 = o0+7
			paths.append(1)
		else:
			o0 = 6-4
			x = x-x
			paths.append(2)
		if m3 >= 2:
			o0 = 2/o0
			paths.append(3)
		else:
			o0 = o0+o0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		m3 = o0**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))