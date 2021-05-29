import numpy as np 

def function(x):

	m3 = 9
	x8 = x
	paths = []
	try:
		if m3 <= 4:
			x8 = x8-m3
			x = x8*x
			x8 = m3-3
			paths.append(1)
		else:
			x = 4/5
			m3 = m3-x8
			m3 = m3/3
			paths.append(2)
		if m3 <= 7:
			m3 = 4+m3
			x8 = 6+7
			x8 = x8+x8
			paths.append(3)
		else:
			m3 = x/3
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))