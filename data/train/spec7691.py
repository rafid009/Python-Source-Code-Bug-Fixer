import numpy as np 

def function(x):

	u5 = 3
	m8 = x
	paths = []
	try:
		if x <= 6:
			x = x-5
			x = 9+x
			paths.append(1)
		else:
			u5 = 4-u5
			m8 = x/1
			paths.append(2)
		if u5 > 7:
			x = u5/6
			m8 = m8-6
			x = x*4
			paths.append(3)
		else:
			x = u5-3
			u5 = 2/7
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))