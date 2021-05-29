import numpy as np 

def function(x):

	m2 = 2
	a5 = x
	x = x
	paths = []
	try:
		if x > 9:
			x = x-8
			x = x-6
			m2 = m2/m2
			paths.append(1)
		else:
			a5 = a5*0
			a5 = a5*a5
			a5 = 5-a5
			paths.append(2)
		if m2 >= 4:
			x = 4/x
			m2 = 8*m2
			a5 = a5/4
			paths.append(3)
		else:
			a5 = a5+1
			a5 = m2+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))