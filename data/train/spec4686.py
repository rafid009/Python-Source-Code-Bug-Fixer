import numpy as np 

def function(x):

	i8 = 8
	m3 = x
	paths = []
	try:
		if i8 > 0:
			x = x+7
			m3 = i8+4
			i8 = x+4
			paths.append(1)
		else:
			i8 = 7-i8
			x = x+2
			m3 = m3+m3
			paths.append(2)
		if i8 <= 0:
			m3 = m3/m3
			i8 = i8/m3
			paths.append(3)
		else:
			i8 = i8-x
			i8 = 0*8
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))