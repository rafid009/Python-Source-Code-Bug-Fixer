import numpy as np 

def function(x):

	o8 = x
	m1 = 0
	paths = []
	try:
		if m1 < 8:
			m1 = m1+2
			o8 = 4-8
			x = x-7
			paths.append(1)
		else:
			x = x/x
			m1 = x/3
			paths.append(2)
		if m1 >= 5:
			x = 4*1
			m1 = o8-x
			paths.append(3)
		else:
			m1 = 6+m1
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))