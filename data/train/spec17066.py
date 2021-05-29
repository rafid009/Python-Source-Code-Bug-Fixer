import numpy as np 

def function(x):

	m6 = 0
	j8 = 9
	paths = []
	try:
		if x >= 7:
			x = x*5
			paths.append(1)
		else:
			x = x-5
			m6 = x-m6
			paths.append(2)
		if m6 > 9:
			m6 = 3-8
			m6 = j8+7
			paths.append(3)
		else:
			j8 = m6*9
			x = 9/x
			j8 = j8/7
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		j8 = m6**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))