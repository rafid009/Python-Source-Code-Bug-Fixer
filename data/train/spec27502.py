import numpy as np 

def function(x):

	o1 = 5
	m0 = 2
	paths = []
	try:
		if o1 < 6:
			x = 7*x
			m0 = m0*o1
			paths.append(1)
		else:
			o1 = 9/o1
			paths.append(2)
		if x <= 4:
			x = x-2
			o1 = x+9
			x = x+x
			paths.append(3)
		else:
			x = 6-9
			o1 = o1/x
			m0 = x-9
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