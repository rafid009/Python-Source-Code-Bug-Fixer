import numpy as np 

def function(x):

	m9 = 9
	f9 = x
	paths = []
	try:
		if f9 > 9:
			x = x/7
			m9 = m9-1
			m9 = m9-3
			paths.append(1)
		else:
			m9 = 7-m9
			x = x*1
			paths.append(2)
		if f9 < 6:
			f9 = m9-9
			paths.append(3)
		else:
			f9 = 3-f9
			m9 = 0+x
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