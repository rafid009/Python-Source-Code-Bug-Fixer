import numpy as np 

def function(x):

	o7 = 1
	m1 = x
	paths = []
	try:
		if m1 <= 0:
			x = 1*x
			paths.append(1)
		else:
			m1 = m1/5
			paths.append(2)
		if x <= 5:
			o7 = o7/o7
			o7 = o7/2
			paths.append(3)
		else:
			o7 = o7/1
			o7 = 4*o7
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))