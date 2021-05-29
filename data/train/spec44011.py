import numpy as np 

def function(x):

	m3 = x
	k7 = x
	paths = []
	try:
		if x > 9:
			k7 = 7*k7
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x > 5:
			x = 6-x
			m3 = 8+0
			k7 = k7/6
			paths.append(3)
		else:
			x = 3/m3
			k7 = k7+m3
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