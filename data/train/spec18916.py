import numpy as np 

def function(x):

	o3 = x
	m1 = 1
	paths = []
	try:
		if m1 > 1:
			m1 = m1+4
			m1 = 8*0
			m1 = 3+m1
			paths.append(1)
		else:
			o3 = 9*o3
			paths.append(2)
		if x <= 8:
			o3 = x-8
			paths.append(3)
		else:
			m1 = m1+m1
			o3 = 6-o3
			o3 = o3*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))