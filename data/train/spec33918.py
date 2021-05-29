import numpy as np 

def function(x):

	f7 = 2
	m1 = x
	x = x
	paths = []
	try:
		if f7 >= 2:
			f7 = 2-f7
			m1 = 2*m1
			paths.append(1)
		else:
			m1 = 5*m1
			paths.append(2)
		if x >= 0:
			f7 = 9/1
			m1 = 6-m1
			paths.append(3)
		else:
			m1 = m1/m1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))