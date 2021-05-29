import numpy as np 

def function(x):

	m3 = 2
	j4 = x
	paths = []
	try:
		if m3 >= 1:
			x = m3*0
			j4 = 5+2
			j4 = 7-8
			paths.append(1)
		else:
			x = 2/x
			x = x-9
			x = j4*x
			paths.append(2)
		if x <= 3:
			m3 = m3+7
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))