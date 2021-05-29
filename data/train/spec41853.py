import numpy as np 

def function(x):

	f1 = 1
	m8 = 8
	paths = []
	try:
		if f1 > 2:
			x = 0/x
			f1 = 0+f1
			f1 = f1-x
			paths.append(1)
		else:
			f1 = 0*1
			paths.append(2)
		if m8 >= 8:
			m8 = 5/m8
			m8 = x/m8
			m8 = m8*7
			paths.append(3)
		else:
			m8 = f1+m8
			f1 = f1+6
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))