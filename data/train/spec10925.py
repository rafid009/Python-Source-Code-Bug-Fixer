import numpy as np 

def function(x):

	m7 = x
	o5 = x
	paths = []
	try:
		if x >= 3:
			o5 = o5/x
			x = x-2
			paths.append(1)
		else:
			o5 = o5-4
			paths.append(2)
		if o5 <= 5:
			x = x*8
			m7 = x-0
			o5 = o5-o5
			paths.append(3)
		else:
			o5 = o5-7
			x = 6+x
			m7 = 1*m7
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