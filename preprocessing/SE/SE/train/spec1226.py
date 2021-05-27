import numpy as np 

def function(x):

	j8 = x
	m8 = 5
	paths = []
	try:
		if x < 7:
			x = 1/x
			j8 = j8/6
			j8 = j8*3
			paths.append(1)
		else:
			m8 = m8/6
			x = x-0
			paths.append(2)
		if x <= 2:
			x = 3/9
			x = x+1
			paths.append(3)
		else:
			m8 = 4*6
			x = m8-m8
			x = 1+j8
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))