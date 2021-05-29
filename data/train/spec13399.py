import numpy as np 

def function(x):

	u5 = 4
	m7 = x
	x = 3
	paths = []
	try:
		if x < 8:
			m7 = 6+m7
			x = x*4
			paths.append(1)
		else:
			u5 = u5+u5
			x = x*4
			x = x-6
			paths.append(2)
		if x <= 8:
			m7 = 9+1
			u5 = u5+4
			paths.append(3)
		else:
			x = m7+x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		u5 = m7**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))