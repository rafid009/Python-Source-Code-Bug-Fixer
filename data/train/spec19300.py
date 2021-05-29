import numpy as np 

def function(x):

	q8 = x
	m9 = x
	paths = []
	try:
		if m9 >= 2:
			x = 4+x
			m9 = m9/x
			paths.append(1)
		else:
			q8 = x/7
			q8 = 4-q8
			x = 2-x
			paths.append(2)
		if x <= 6:
			q8 = q8+9
			x = 9/x
			paths.append(3)
		else:
			q8 = q8*9
			m9 = 6-m9
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