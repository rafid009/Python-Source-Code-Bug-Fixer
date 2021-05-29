import numpy as np 

def function(x):

	j1 = x
	m3 = x
	paths = []
	try:
		if j1 >= 2:
			m3 = j1*m3
			paths.append(1)
		else:
			x = j1+2
			paths.append(2)
		if m3 >= 2:
			j1 = j1+j1
			paths.append(3)
		else:
			j1 = j1-4
			j1 = j1/2
			x = m3*x
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))