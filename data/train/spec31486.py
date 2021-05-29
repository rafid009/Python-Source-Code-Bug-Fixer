import numpy as np 

def function(x):

	m5 = x
	j9 = x
	x = x
	paths = []
	try:
		if x < 3:
			m5 = 3*m5
			x = x*x
			paths.append(1)
		else:
			m5 = 5+m5
			paths.append(2)
		if j9 < 3:
			x = x-3
			paths.append(3)
		else:
			x = 4*m5
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		j9 = j9**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))