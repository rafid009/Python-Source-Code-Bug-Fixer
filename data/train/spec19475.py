import numpy as np 

def function(x):

	i9 = x
	m1 = 5
	paths = []
	try:
		if m1 > 3:
			x = m1*5
			i9 = 5+i9
			x = x+x
			paths.append(1)
		else:
			i9 = 0-i9
			i9 = i9+4
			paths.append(2)
		if x < 2:
			i9 = i9*7
			x = i9+x
			paths.append(3)
		else:
			m1 = 9+3
			x = x*0
			m1 = 7*7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		x = i9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))