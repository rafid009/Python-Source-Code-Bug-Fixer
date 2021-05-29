import numpy as np 

def function(x):

	m1 = x
	o5 = 6
	paths = []
	try:
		if x >= 2:
			x = o5*2
			paths.append(1)
		else:
			m1 = 1*m1
			o5 = o5-8
			paths.append(2)
		if o5 < 3:
			o5 = 6+6
			o5 = x/4
			paths.append(3)
		else:
			o5 = 4-o5
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