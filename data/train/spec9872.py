import numpy as np 

def function(x):

	a5 = 6
	m4 = 7
	paths = []
	try:
		if m4 > 7:
			m4 = 4/6
			paths.append(1)
		else:
			a5 = 3-a5
			a5 = 4-a5
			paths.append(2)
		if a5 < 4:
			a5 = 8-a5
			a5 = 4+4
			x = 8+6
			paths.append(3)
		else:
			x = 4+x
			m4 = 8-m4
			a5 = x+a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))