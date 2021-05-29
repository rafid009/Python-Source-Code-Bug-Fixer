import numpy as np 

def function(x):

	j6 = x
	m6 = 2
	paths = []
	try:
		if m6 <= 0:
			x = m6-7
			x = 1-m6
			x = x+3
			paths.append(1)
		else:
			j6 = j6*4
			x = x+6
			paths.append(2)
		if m6 < 9:
			x = 2*x
			m6 = m6+4
			paths.append(3)
		else:
			j6 = j6+m6
			j6 = x/j6
			x = x-j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))