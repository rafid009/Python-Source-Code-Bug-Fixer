import numpy as np 

def function(x):

	f3 = x
	m8 = 1
	paths = []
	try:
		if x <= 6:
			x = x+2
			x = 7*x
			x = 3-x
			paths.append(1)
		else:
			f3 = f3*8
			paths.append(2)
		if x < 2:
			m8 = m8+m8
			m8 = f3+x
			paths.append(3)
		else:
			f3 = 9+0
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))