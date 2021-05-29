import numpy as np 

def function(x):

	m3 = x
	a0 = x
	paths = []
	try:
		if m3 >= 9:
			x = x+2
			x = x/6
			paths.append(1)
		else:
			a0 = 7*9
			a0 = x/3
			paths.append(2)
		if m3 > 9:
			a0 = a0-4
			a0 = a0+x
			a0 = 3-a0
			paths.append(3)
		else:
			a0 = 0+9
			x = 3*9
			a0 = x*7
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		a0 = m3**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))