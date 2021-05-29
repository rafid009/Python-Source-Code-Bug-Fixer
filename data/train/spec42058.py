import numpy as np 

def function(x):

	f4 = 6
	m9 = x
	paths = []
	try:
		if f4 >= 2:
			m9 = 3+m9
			f4 = f4-m9
			m9 = 5+m9
			paths.append(1)
		else:
			x = x+x
			x = x/3
			paths.append(2)
		if f4 < 3:
			f4 = x/2
			paths.append(3)
		else:
			x = x-1
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