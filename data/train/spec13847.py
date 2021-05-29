import numpy as np 

def function(x):

	f1 = 7
	m2 = 2
	paths = []
	try:
		if m2 <= 3:
			m2 = x*f1
			f1 = f1+f1
			paths.append(1)
		else:
			m2 = m2/2
			f1 = 5/f1
			paths.append(2)
		if f1 > 6:
			x = x/x
			x = 7-9
			f1 = f1+m2
			paths.append(3)
		else:
			f1 = 8*f1
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))