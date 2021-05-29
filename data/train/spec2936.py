import numpy as np 

def function(x):

	e3 = 4
	m5 = x
	paths = []
	try:
		if e3 < 3:
			x = m5+x
			paths.append(1)
		else:
			x = e3-m5
			paths.append(2)
		if m5 >= 4:
			e3 = 2-e3
			x = 0-0
			paths.append(3)
		else:
			x = x/3
			e3 = e3-5
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))