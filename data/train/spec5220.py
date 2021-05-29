import numpy as np 

def function(x):

	y7 = 4
	m3 = 1
	x = x
	paths = []
	try:
		if m3 <= 9:
			y7 = y7+7
			m3 = x+6
			paths.append(1)
		else:
			y7 = x-2
			y7 = y7*1
			x = y7-y7
			paths.append(2)
		if m3 >= 4:
			m3 = x+8
			x = m3-9
			paths.append(3)
		else:
			y7 = x*x
			m3 = x+7
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))