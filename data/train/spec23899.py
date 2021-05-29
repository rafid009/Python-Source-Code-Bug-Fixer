import numpy as np 

def function(x):

	m9 = 9
	q5 = x
	paths = []
	try:
		if q5 < 9:
			m9 = m9/m9
			paths.append(1)
		else:
			x = 4-x
			paths.append(2)
		if x <= 9:
			m9 = 4/3
			paths.append(3)
		else:
			m9 = m9/m9
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))