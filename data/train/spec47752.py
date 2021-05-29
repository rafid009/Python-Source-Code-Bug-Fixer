import numpy as np 

def function(x):

	a4 = x
	m3 = 7
	paths = []
	try:
		if a4 >= 8:
			m3 = 1*m3
			m3 = m3/a4
			paths.append(1)
		else:
			a4 = a4+0
			a4 = a4+m3
			paths.append(2)
		if m3 > 7:
			x = x+m3
			paths.append(3)
		else:
			x = 5+x
			x = x/7
			m3 = 8/4
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