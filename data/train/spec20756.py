import numpy as np 

def function(x):

	m5 = 9
	o0 = 4
	paths = []
	try:
		if o0 < 6:
			x = 7*x
			paths.append(1)
		else:
			x = x*o0
			paths.append(2)
		if o0 > 4:
			m5 = 7/m5
			o0 = 7+o0
			paths.append(3)
		else:
			o0 = 7-m5
			x = x*1
			m5 = 5*m5
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))