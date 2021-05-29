import numpy as np 

def function(x):

	a2 = x
	m1 = x
	x = x
	paths = []
	try:
		if x >= 5:
			x = m1+1
			x = x/9
			a2 = m1*m1
			paths.append(1)
		else:
			a2 = a2+5
			paths.append(2)
		if m1 > 6:
			m1 = x-m1
			x = 9+x
			paths.append(3)
		else:
			m1 = m1-9
			a2 = a2-7
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))