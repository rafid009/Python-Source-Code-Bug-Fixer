import numpy as np 

def function(x):

	m3 = 0
	a7 = x
	paths = []
	try:
		if a7 <= 1:
			x = x+1
			x = x/1
			m3 = a7/1
			paths.append(1)
		else:
			a7 = a7*2
			m3 = 6-a7
			m3 = x/m3
			paths.append(2)
		if x < 2:
			x = x+3
			paths.append(3)
		else:
			x = 4-5
			m3 = m3-a7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))