import numpy as np 

def function(x):

	m1 = 0
	i5 = x
	x = x
	paths = []
	try:
		if x >= 9:
			m1 = m1*i5
			x = i5*x
			i5 = i5-i5
			paths.append(1)
		else:
			m1 = x*4
			x = x/x
			paths.append(2)
		if i5 <= 6:
			i5 = 0+8
			m1 = m1/4
			x = 4-7
			paths.append(3)
		else:
			i5 = i5*m1
			i5 = i5*m1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))