import numpy as np 

def function(x):

	f4 = x
	m6 = x
	paths = []
	try:
		if m6 > 4:
			f4 = f4-8
			m6 = f4*1
			f4 = 8/f4
			paths.append(1)
		else:
			x = 6+x
			f4 = 5+f4
			paths.append(2)
		if f4 >= 2:
			x = f4*x
			paths.append(3)
		else:
			x = x*7
			m6 = x*m6
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))