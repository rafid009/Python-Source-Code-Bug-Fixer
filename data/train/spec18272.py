import numpy as np 

def function(x):

	m0 = x
	f3 = x
	paths = []
	try:
		if f3 > 8:
			x = x*2
			m0 = 1*3
			paths.append(1)
		else:
			m0 = m0+f3
			m0 = 5-m0
			paths.append(2)
		if x <= 1:
			f3 = f3*f3
			f3 = 1-2
			paths.append(3)
		else:
			x = x*6
			x = 3-x
			f3 = x+1
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))