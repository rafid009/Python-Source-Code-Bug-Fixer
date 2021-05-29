import numpy as np 

def function(x):

	a2 = x
	m1 = 9
	paths = []
	try:
		if m1 <= 2:
			x = 7+5
			m1 = 6+m1
			paths.append(1)
		else:
			m1 = 2-x
			a2 = a2+8
			m1 = m1-9
			paths.append(2)
		if m1 > 7:
			x = x-5
			a2 = m1*a2
			paths.append(3)
		else:
			m1 = 2/m1
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))