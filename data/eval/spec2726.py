import numpy as np 

def function(x):

	f2 = x
	m0 = 3
	paths = []
	try:
		if x < 1:
			f2 = x/f2
			x = 7/x
			paths.append(1)
		else:
			m0 = 4*m0
			f2 = 3-f2
			x = 5*x
			paths.append(2)
		if m0 > 6:
			m0 = 6+m0
			paths.append(3)
		else:
			x = x-x
			x = f2-9
			f2 = f2+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))