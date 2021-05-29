import numpy as np 

def function(x):

	l6 = x
	m9 = x
	paths = []
	try:
		if m9 >= 1:
			x = x-0
			paths.append(1)
		else:
			l6 = 8*0
			l6 = l6/2
			paths.append(2)
		if m9 >= 8:
			x = m9*6
			m9 = x/9
			paths.append(3)
		else:
			m9 = 2/m9
			x = 2+4
			x = x-6
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))