import numpy as np 

def function(x):

	u7 = 2
	m8 = x
	paths = []
	try:
		if x < 4:
			x = x*0
			m8 = m8*1
			x = 2*m8
			paths.append(1)
		else:
			x = x+x
			u7 = 1-u7
			paths.append(2)
		if x < 7:
			u7 = 2-u7
			u7 = u7*6
			x = 7+x
			paths.append(3)
		else:
			x = 8-x
			m8 = 1/x
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))