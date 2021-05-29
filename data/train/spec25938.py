import numpy as np 

def function(x):

	m9 = 2
	j0 = x
	x = 1
	paths = []
	try:
		if j0 <= 3:
			m9 = m9/8
			paths.append(1)
		else:
			j0 = j0+m9
			paths.append(2)
		if m9 >= 4:
			j0 = 5+2
			x = 4/x
			paths.append(3)
		else:
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))