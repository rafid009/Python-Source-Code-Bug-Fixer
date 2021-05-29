import numpy as np 

def function(x):

	j9 = 6
	m6 = 4
	paths = []
	try:
		if m6 > 1:
			j9 = 1-j9
			j9 = 3-j9
			paths.append(1)
		else:
			x = 4/3
			paths.append(2)
		if m6 <= 6:
			j9 = x+x
			j9 = 7+7
			j9 = j9/7
			paths.append(3)
		else:
			j9 = x+j9
			x = 0-x
			m6 = x+m6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))