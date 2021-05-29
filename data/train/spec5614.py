import numpy as np 

def function(x):

	m4 = x
	f1 = x
	paths = []
	try:
		if x <= 5:
			m4 = m4-3
			x = 6+x
			m4 = 1*m4
			paths.append(1)
		else:
			f1 = f1+0
			x = 2/7
			paths.append(2)
		if m4 >= 9:
			m4 = 9/2
			paths.append(3)
		else:
			f1 = 3/f1
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))