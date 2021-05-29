import numpy as np 

def function(x):

	d8 = x
	m2 = x
	paths = []
	try:
		if x < 0:
			x = 6-7
			d8 = 0+d8
			x = 5/x
			paths.append(1)
		else:
			x = 5/3
			d8 = m2+m2
			paths.append(2)
		if m2 <= 4:
			m2 = 5/m2
			m2 = x-d8
			paths.append(3)
		else:
			x = 9/9
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))