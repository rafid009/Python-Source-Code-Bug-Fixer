import numpy as np 

def function(x):

	y6 = 8
	m9 = 5
	paths = []
	try:
		if y6 <= 6:
			y6 = 3-7
			y6 = y6*x
			y6 = y6/9
			paths.append(1)
		else:
			y6 = 3/x
			x = x*0
			m9 = 3-0
			paths.append(2)
		if y6 >= 4:
			m9 = 9/m9
			m9 = 1*3
			paths.append(3)
		else:
			m9 = m9-4
			x = 7/8
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))