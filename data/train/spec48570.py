import numpy as np 

def function(x):

	a4 = x
	m6 = 3
	paths = []
	try:
		if a4 > 2:
			a4 = 8*0
			a4 = 9+a4
			paths.append(1)
		else:
			m6 = m6/1
			paths.append(2)
		if x < 7:
			m6 = m6*9
			paths.append(3)
		else:
			m6 = m6+m6
			a4 = a4*1
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))