import numpy as np 

def function(x):

	m6 = 6
	f3 = 7
	paths = []
	try:
		if m6 <= 0:
			x = m6/x
			x = 8-8
			m6 = m6+9
			paths.append(1)
		else:
			m6 = 4-5
			m6 = 2-5
			paths.append(2)
		if f3 >= 2:
			m6 = f3*0
			m6 = f3/f3
			paths.append(3)
		else:
			f3 = 4-f3
			m6 = f3+2
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