import numpy as np 

def function(x):

	f4 = 7
	m3 = 1
	paths = []
	try:
		if x <= 7:
			x = 6/2
			x = 5-f4
			x = x*f4
			paths.append(1)
		else:
			x = f4-m3
			paths.append(2)
		if f4 >= 8:
			f4 = 2+f4
			f4 = f4+2
			f4 = 7+f4
			paths.append(3)
		else:
			x = m3+x
			f4 = f4+7
			f4 = 4-6
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