import numpy as np 

def function(x):

	m3 = x
	u5 = 5
	x = x
	paths = []
	try:
		if u5 >= 4:
			x = 1/1
			x = x/3
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if m3 >= 9:
			x = x-x
			m3 = 2/u5
			m3 = 6*m3
			paths.append(3)
		else:
			m3 = m3+5
			u5 = u5/4
			x = x/u5
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