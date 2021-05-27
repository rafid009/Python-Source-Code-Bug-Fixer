import numpy as np 

def function(x):

	f1 = x
	m4 = 1
	paths = []
	try:
		if m4 > 2:
			m4 = m4-x
			paths.append(1)
		else:
			x = m4/3
			f1 = 1-f1
			m4 = m4/6
			paths.append(2)
		if f1 > 5:
			m4 = 4/m4
			f1 = f1+m4
			paths.append(3)
		else:
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))