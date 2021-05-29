import numpy as np 

def function(x):

	u5 = x
	m3 = 6
	paths = []
	try:
		if u5 >= 6:
			m3 = 8*m3
			m3 = 9-m3
			x = 7/5
			paths.append(1)
		else:
			x = x/m3
			m3 = x/7
			u5 = u5-m3
			paths.append(2)
		if x >= 5:
			u5 = 2-x
			u5 = u5+8
			m3 = m3-x
			paths.append(3)
		else:
			x = u5+1
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))