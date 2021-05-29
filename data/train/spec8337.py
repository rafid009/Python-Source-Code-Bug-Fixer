import numpy as np 

def function(x):

	m3 = 8
	f6 = 0
	paths = []
	try:
		if m3 >= 1:
			m3 = f6*1
			paths.append(1)
		else:
			f6 = 9-f6
			paths.append(2)
		if x >= 7:
			x = x/6
			m3 = 9+m3
			paths.append(3)
		else:
			f6 = 9+f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))