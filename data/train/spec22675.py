import numpy as np 

def function(x):

	m7 = x
	a7 = x
	paths = []
	try:
		if x <= 9:
			m7 = m7+1
			m7 = 3/a7
			paths.append(1)
		else:
			x = x/6
			x = 5-0
			m7 = 8+5
			paths.append(2)
		if x < 1:
			x = x*9
			x = m7*x
			paths.append(3)
		else:
			a7 = a7+0
			a7 = 9*a7
			a7 = 9/a7
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		a7 = m7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))