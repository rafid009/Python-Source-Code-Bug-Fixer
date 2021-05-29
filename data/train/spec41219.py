import numpy as np 

def function(x):

	m3 = x
	f8 = x
	x = 1
	paths = []
	try:
		if f8 >= 0:
			m3 = 9+9
			x = 1-x
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if m3 <= 2:
			m3 = m3+7
			x = 5*6
			x = 0+x
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))