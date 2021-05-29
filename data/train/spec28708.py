import numpy as np 

def function(x):

	m3 = x
	e5 = 7
	x = 8
	paths = []
	try:
		if x < 6:
			e5 = e5*6
			e5 = e5*x
			e5 = e5*0
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if x > 4:
			m3 = x*m3
			x = 5-x
			paths.append(3)
		else:
			x = 7*x
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