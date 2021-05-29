import numpy as np 

def function(x):

	m5 = 0
	o5 = x
	paths = []
	try:
		if m5 <= 9:
			o5 = x*5
			o5 = o5+2
			o5 = o5*3
			paths.append(1)
		else:
			o5 = 1*7
			paths.append(2)
		if x >= 4:
			m5 = x*m5
			m5 = 8-o5
			paths.append(3)
		else:
			o5 = o5/3
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))