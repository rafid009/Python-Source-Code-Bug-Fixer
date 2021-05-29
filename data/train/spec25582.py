import numpy as np 

def function(x):

	m4 = 0
	n3 = x
	paths = []
	try:
		if m4 >= 2:
			x = x/m4
			x = 2+x
			n3 = n3-x
			paths.append(1)
		else:
			m4 = m4+m4
			x = 7+m4
			x = x+5
			paths.append(2)
		if m4 >= 2:
			n3 = n3+1
			n3 = 8/n3
			paths.append(3)
		else:
			x = x/x
			m4 = 4*m4
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))