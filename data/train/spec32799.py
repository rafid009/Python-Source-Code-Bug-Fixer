import numpy as np 

def function(x):

	o2 = x
	m9 = x
	paths = []
	try:
		if x >= 2:
			o2 = o2-m9
			o2 = 9-x
			paths.append(1)
		else:
			o2 = o2-0
			m9 = x*m9
			paths.append(2)
		if o2 >= 8:
			x = 7*3
			x = 8/o2
			m9 = 0/m9
			paths.append(3)
		else:
			o2 = o2+7
			x = 5+x
			o2 = x-1
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