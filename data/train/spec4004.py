import numpy as np 

def function(x):

	m9 = 4
	v9 = x
	paths = []
	try:
		if x <= 3:
			x = x-2
			x = x-m9
			v9 = m9/v9
			paths.append(1)
		else:
			m9 = m9+m9
			v9 = m9+9
			m9 = 5/m9
			paths.append(2)
		if v9 < 9:
			x = 3/m9
			m9 = 0-7
			paths.append(3)
		else:
			m9 = m9+v9
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))