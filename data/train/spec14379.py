import numpy as np 

def function(x):

	a5 = 2
	m4 = x
	paths = []
	try:
		if m4 >= 2:
			a5 = 7*0
			m4 = a5-9
			paths.append(1)
		else:
			m4 = m4*3
			x = x*4
			paths.append(2)
		if m4 > 4:
			a5 = x+8
			m4 = 0-1
			paths.append(3)
		else:
			a5 = 1-a5
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))