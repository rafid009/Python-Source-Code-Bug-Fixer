import numpy as np 

def function(x):

	i9 = x
	m2 = 6
	paths = []
	try:
		if m2 >= 7:
			i9 = 5-8
			i9 = i9*8
			x = x*x
			paths.append(1)
		else:
			x = 4+7
			m2 = 5*4
			paths.append(2)
		if i9 <= 6:
			m2 = i9/m2
			x = x+x
			paths.append(3)
		else:
			i9 = 5+i9
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))