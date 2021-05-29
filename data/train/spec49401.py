import numpy as np 

def function(x):

	m2 = 3
	o0 = 5
	paths = []
	try:
		if x < 4:
			o0 = x-o0
			x = 8*2
			paths.append(1)
		else:
			o0 = o0+3
			o0 = m2*o0
			paths.append(2)
		if x <= 9:
			o0 = o0-6
			m2 = m2*8
			x = x/7
			paths.append(3)
		else:
			o0 = o0+o0
			x = x*4
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))