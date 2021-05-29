import numpy as np 

def function(x):

	m2 = x
	o1 = 5
	x = x
	paths = []
	try:
		if m2 < 4:
			x = x-m2
			paths.append(1)
		else:
			o1 = o1-7
			m2 = o1-m2
			paths.append(2)
		if m2 < 2:
			x = x+6
			m2 = x-m2
			paths.append(3)
		else:
			o1 = 4-o1
			m2 = 2*m2
			o1 = o1*1
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))