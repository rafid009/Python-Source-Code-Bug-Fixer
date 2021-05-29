import numpy as np 

def function(x):

	m4 = x
	j6 = x
	paths = []
	try:
		if m4 > 5:
			x = 9/7
			paths.append(1)
		else:
			x = 2/x
			x = x+9
			x = 5/m4
			paths.append(2)
		if m4 > 8:
			m4 = m4/9
			paths.append(3)
		else:
			x = 3*x
			j6 = 4-j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))