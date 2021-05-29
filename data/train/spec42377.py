import numpy as np 

def function(x):

	x6 = x
	m7 = 5
	paths = []
	try:
		if x >= 1:
			x = x*x6
			paths.append(1)
		else:
			m7 = x6*m7
			x6 = 2/x
			x6 = x6+x6
			paths.append(2)
		if m7 >= 2:
			x = x6*x
			x6 = x6*1
			x = x/2
			paths.append(3)
		else:
			x6 = x/x
			x = x/x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		x6 = m7**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))