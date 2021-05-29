import numpy as np 

def function(x):

	m4 = x
	a5 = x
	paths = []
	try:
		if a5 >= 5:
			m4 = m4*8
			a5 = a5*a5
			m4 = 2/8
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if m4 > 4:
			x = x/1
			x = x-0
			paths.append(3)
		else:
			a5 = m4-a5
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